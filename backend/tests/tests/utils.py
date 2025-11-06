import json
import logging
import requests
from requests import Response
from json import JSONDecodeError
import allure
from allure_commons.types import AttachmentType


class APIClient:
    def __init__(self, base_url="http://127.0.0.1:8000/api/v1", default_headers=None):
        self.base_url = base_url
        self.default_headers = default_headers or {}

    def response_logging(response: Response):
        logging.info("Request: " + response.request.url)
        if response.request.body:
            logging.info("INFO Request body: " + str(response.request.body))
        logging.info("Request headers: " + str(response.request.headers))
        logging.info("Response code: " + str(response.status_code))
        logging.info("Response: " + str(response.text))


def _get_request_body(response: Response):
    try:
        if response.request.body:
            return json.dumps(
                json.loads(response.request.body), indent=4, ensure_ascii=True
            )
    except (JSONDecodeError, TypeError):
        return str(response.request.body)
    return ""


def _get_response_body(response: Response):
    try:
        return json.dumps(response.json(), indent=4, ensure_ascii=True)
    except JSONDecodeError:
        return response.text


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=_get_request_body(response),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

    if response.content:
        allure.attach(
            body=_get_response_body(response),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


def api_request(
    endpoint,
    method,
    base_api_url="http://127.0.0.1:8000/api/v1",
    data=None,
    params=None,
    json=None,
    headers=None,
    expected_status=None,
) -> dict:
    # Устанавливаем expected_status по умолчанию в зависимости от метода
    if expected_status is None:
        if method.lower() == "get":
            expected_status = 200
        elif method.lower() == "post":
            expected_status = 201

    url = f"{base_api_url}{endpoint}"
    response = requests.request(
        method, url, data=data, params=params, json=json, headers=headers
    )

    APIClient.response_logging(response)
    response_attaching(response)

    # Проверяем expected
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, but got {response.status_code}. "
        f"Response: {response.text}"
    )

    # Возвращаем JSON
    return response.json()