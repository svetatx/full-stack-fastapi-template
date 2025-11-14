
from utils import APIClient
from http import HTTPMethod, HTTPStatus

BASE_URL = "http://127.0.0.1:8000/api/v1"


class UsersClient:
    def __init__(self, client: APIClient):
        self.client = client

    def register_user(self, email: str, password: str, full_name: str):
        return self.client.post(
            endpoint="/users/signup",
            json={"email": email, "password": password, "full_name": full_name},
            expected_status=HTTPStatus.OK,
        )

    def get_user_by_id(self, user_id: str):
        return self.client.get(
            endpoint=f"/users/{user_id}",
        )