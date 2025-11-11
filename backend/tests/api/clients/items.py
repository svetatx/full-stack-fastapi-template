from http import HTTPMethod, HTTPStatus
from utils import api_request

BASE_URL = "http://127.0.0.1:8000/api/v1"


# POST: создать item
def create_item(title: str, description: str, headers: dict):
    return api_request(
        endpoint="/items/",
        method="POST",
        json={"title": title, "description": description},
        expected_status=HTTPStatus.OK,
        header=headers
    )

def get_item_by_id(item_id: int, headers: dict):
    return api_request(
        endpoint=f"/items/{item_id}",
        method="GET",
        headers=headers,
        expected_status=HTTPStatus.OK,
    )

def get_item(title: str, description: str, headers: dict):
    return api_request(
        endpoint=f"/items/",
        method="GET",
        json={"title": title, "description": description},
        expected_status=HTTPStatus.OK,
        header=headers
    )

def update_item(item_id: int, title: str, description: str, headers: dict):
    return api_request(
        endpoint=f"/items/{item_id}",
        method="PUT",
        json={"title": title, "description": description},
        expected_status=HTTPStatus.OK,
        headers=headers,
    )

def delete_item(item_id: int, headers: dict):
    return api_request(
        endpoint=f"/items/{item_id}",
        method="DELETE",
        headers=headers,
        expected_status=HTTPStatus.OK,
    )