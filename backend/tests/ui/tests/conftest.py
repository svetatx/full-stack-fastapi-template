import random
import string
import pytest
from http import HTTPStatus
from utils import APIClient
from clients.users import UsersClient
from clients.items import ItemsClient
from clients.users import register_user  # твой клиент
from utils import api_request  # общий helper для HTTP

@pytest.fixture
def api_client() -> APIClient:
    return APIClient(base_url="http://127.0.0.1:8000/api/v1")

@pytest.fixture
def authenticated_api_client(auth_headers) -> APIClient:
    return APIClient(
        base_url="http://127.0.0.1:8000/api/v1", default_headers=auth_headers
    )

@pytest.fixture
def users_api_client(api_client) -> UsersClient:
    return UsersClient(api_client)

@pytest.fixture 
def users_authenticated_api_client(authenticated_api_client) -> UsersClient:
    return UsersClient(authenticated_api_client)

@pytest.fixture 
def items_authenticated_api_client(authenticated_api_client) -> ItemsClient:
    return ItemsClient(authenticated_api_client)


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
def auth_headers(created_user, api_client: APIClient, user_payload):
    got = api_client.post(
        endpoint="/login/access-token",
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

@pytest.fixture()
def item_payload():
    return {
        "title": f"demo_item_{''.join(random.choices(string.ascii_lowercase, k=5))}",
        "description": "created from API test",
    }
