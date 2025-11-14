from http import HTTPStatus
from utils import APIClient


class ItemsClient:
    def __init__(self, client: APIClient):
        self.client = client

    def create_item(self, title: str, description: str):
        return self.client.post(
            endpoint="/items/",
            json={"title": title, "description": description},
            expected_status=HTTPStatus.OK,
        )

    def get_item_by_id(self, item_id: int):
        return self.client.get(
            endpoint=f"/items/{item_id}",
            expected_status=HTTPStatus.OK,
        )

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.client.get(
            endpoint="/items/",
            params={"skip": skip, "limit": limit},
            expected_status=HTTPStatus.OK,
        )

    def update_item(self, item_id: int, title: str, description: str):
        return self.client.put(
            endpoint=f"/items/{item_id}",
            json={"title": title, "description": description},
            expected_status=HTTPStatus.OK,
        )

    def delete_item(self, item_id: int):
        return self.client.delete(
            endpoint=f"/items/{item_id}",
            expected_status=HTTPStatus.OK,
        )