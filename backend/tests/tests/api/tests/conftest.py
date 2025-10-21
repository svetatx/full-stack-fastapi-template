import os
import random
import string
import pytest
from http import HTTPStatus
from api.clients.users import register_user  # твой клиент
from api.utils import api_request            # общий helper для HTTP

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def _rand_email(prefix="sveta"):
    return f"{prefix}{''.join(random.choices(string.digits, k=5))}@example.com"

@pytest.fixture()
def user_payload():
    return {
        "email": _rand_email(),
        "password": "password123",
        "full_name": "qa_user",
    }

# 1) Авторизация → токен → заголовки
@pytest.fixture()
def auth_headers(user_payload):
    """
    Создаём пользователя (на случай если нет),
    логинимся и возвращаем headers с Bearer-токеном.
    """
    # гарантируем, что юзер зарегистрирован (если уже есть — ок)
    try:
        register_user(**user_payload)
    except AssertionError:
        # если твой register_user валидирует 200 и API вернул, например, 409 — это не критично для логина
        pass

    # ⚠️ Если у тебя другой путь логина или форма данных — см. комментарий ниже.
    login_resp = api_request(
        endpoint="/auth/login",
        method="POST",
        json={"email": user_payload["email"], "password": user_payload["password"]},
        expected_status=HTTPStatus.OK,
    )
    token = login_resp.get("access_token") or login_resp.get("token")
    assert token, f"No token in login response: {login_resp}"
    return {"Authorization": f"Bearer {token}"}

# 2) Создание пользователя → JSON с id
@pytest.fixture()
def created_user(user_payload):
    data = register_user(**user_payload)
    assert data.get("is_active") is True
    return data  # ожидаем ключи: id, email, full_name, is_active