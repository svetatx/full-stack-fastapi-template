import json
import uuid
from json.decoder import JSONDecodeError
from typing import Any
from allure_commons.types import AttachmentType
from httpx import URL
import allure
from jinja2 import Environment, PackageLoader, TemplateError, select_autoescape

import httpx
import structlog
from curlify2 import Curlify

from .configuration import Configuration


class AllureLogging:
    def __init__(self, configuration: Any) -> None:
        self.configuration = configuration
        self.env = Environment(
            loader=PackageLoader("testing"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    @staticmethod
    def _get_request_body(request: httpx.Request) -> str:
        try:
            if request.content:
                return json.dumps(json.loads(request.content), indent=4)
        except (JSONDecodeError, TypeError):
            return str(request.content)
        return ""

    @staticmethod
    def _get_response_body(response: httpx.Response) -> dict:
        try:
            body = response.json()
            return {"body": json.dumps(body, indent=4), "is_json": True}
        except JSONDecodeError:
            return {"body": response.text, "is_json": False}

    def _render_template(self, template_name: str, context: dict) -> str:
        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except TemplateError as e:
            return f"Template error: {e!s}"

    def log_to_allure(self, response: httpx.Response) -> None:
        curl_command = Curlify(response.request).to_curl()

        request_data = {
            "method": response.request.method,
            "url": str(response.request.url),
            "headers": dict(response.request.headers),
            "body": self._get_request_body(response.request),
            "curl": curl_command,
        }

        request_html = self._render_template(
            "http-request.html", {"request": request_data, "curl": curl_command}
        )

        response_time = response.elapsed.total_seconds() * 1000
        response_body = self._get_response_body(response)

        response_data = {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response_body["body"],
            "is_json": response_body["is_json"],
            "time": f"{response_time:.2f}",
        }

        response_html = self._render_template(
            "http-response.html", {"response": response_data}
        )

        with allure.step(f"{response.request.method} {response.request.url}"):
            allure.attach(
                body=request_html,
                name="Request",
                attachment_type=AttachmentType.HTML,
                extension=".html",
            )
            allure.attach(
                body=response_html,
                name=f"Response {response.status_code}",
                attachment_type=AttachmentType.HTML,
                extension=".html",
            )


class Logging:
    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration
        self.log = structlog.get_logger(__name__).bind(service="api")

    def log_request(self, method: str, url: str, **kwargs: Any) -> None:
        log = self.log.bind(event_id=str(uuid.uuid4()))
        json_data = kwargs.get("json")
        content = kwargs.get("content")
        try:
            if content:
                json_data = json.loads(content)
        except JSONDecodeError:
            ...

        msg = dict(
            event="Request",
            method=method,
            path=url,
            host=self.configuration.base_url,
            params=kwargs.get("params"),
            headers=kwargs.get("headers"),
            data=kwargs.get("data"),
        )

        if isinstance(json_data, dict):
            msg["json"] = json_data

        log.msg(**msg)

    def log_response(self, response: httpx.Response) -> None:
        log = self.log.bind(event_id=str(uuid.uuid4()))
        curl = Curlify(response.request).to_curl()
        print(curl)
        log.msg(
            event="Response",
            status_code=response.status_code,
            headers=dict(response.headers),
            content=self._get_json(response),
        )

    @staticmethod
    def _get_json(response: httpx.Response) -> dict[str, Any] | bytes:
        try:
            return response.json()
        except JSONDecodeError:
            return response.content


# class Client(httpx.Client):
#     def __init__(self, configuration: Configuration) -> None:
#         self.configuration = configuration
#         super().__init__(
#             base_url=self.configuration.base_url, **self.configuration.kwargs
#         )
#         self._logger = Logging(self.configuration)

#     def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:  # type: ignore
#         if not self.configuration.disable_log:
#             self._logger.log_request(method, url, **kwargs)

#         response = super().request(method, url, **kwargs)

#         if not self.configuration.disable_log:
#             self._logger.log_response(response)

#         response.raise_for_status()
#         return response


class Client(httpx.Client):
    def __init__(self, configuration: Any) -> None:
        self.configuration = configuration
        super().__init__(
            base_url=self.configuration.base_url, **self.configuration.kwargs
        )
        self._logger = Logging(self.configuration)
        self._allure_logger = AllureLogging(self.configuration)

    def request(self, method: str, url: str | URL, **kwargs: Any) -> httpx.Response:
        if not self.configuration.disable_log:
            self._logger.log_request(method, str(url), **kwargs)

        response = super().request(method, url, **kwargs)

        if not self.configuration.disable_log:
            self._logger.log_response(response)

        if not self.configuration.disable_allure_log:
            self._allure_logger.log_to_allure(response)

        return response
