from api.utils import api_request
from http import HTTPMethod, HTTPStatus

BASE_URL = "http://127.0.0.1:8000/api/v1"


# POST: создать пользователя
def register_user(email: str, password: str, full_name: str):
    return api_request(
        endpoint="/users/signup",
        method="POST",
        json={"email": email, "password": password, "full_name": full_name},
        expected_status=200,
    )


def get_user_by_id(user_id: str, headers):
    return api_request(
        endpoint=f"/users/{user_id}",
        method=HTTPMethod.GET,
        expected_status=HTTPStatus.OK,
        headers=headers,
    )
def read_users(headers=None):
    return api_request(
        endpoint="/users",
        method=HTTPMethod.GET,
        expected_status=HTTPStatus.OK,
        headers=headers,
    )