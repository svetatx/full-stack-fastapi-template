import random
import string
import pytest
from http import HTTPStatus
from api.clients.users import register_user  # твой клиент
from api.utils import api_request  # общий helper для HTTP


def _rand_email(prefix="sveta"):
    return f"{prefix}{''.join(random.choices(string.digits, k=5))}@example.com"


@pytest.fixture()
def user_payload():
    return {
        "email": _rand_email(),
        "password": "password123",
        "full_name": "qa_user",
    }


@pytest.fixture()
def auth_headers(user_payload):
    got = api_request(
        endpoint="/login/access-token",
        method="POST",
        data={
            "username": user_payload["email"],
            "password": user_payload["password"],
        },
        expected_status=HTTPStatus.OK,
    )
    return {"Authorization": f"Bearer {got['access_token']}"}


@pytest.fixture()
def created_user(user_payload):
    data = register_user(**user_payload)
    assert data.get("is_active") is True
    return data  # ожидаем ключи: id, email, full_name, is_active
