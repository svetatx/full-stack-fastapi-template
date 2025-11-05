from backend.http import HTTPMethod, HTTPStatus

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