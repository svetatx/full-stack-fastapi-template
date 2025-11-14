from random import randint
from clients.users import UsersClient


def test_register_user(users_api_client: UsersClient):
    response = users_api_client.register_user(
        email=f"svetlana{randint(1, 1000)}@gmai.com",
        password="Password123",
        full_name="qa_user1",
    )

    assert response["is_active"] == True
    assert response["is_superuser"] == False


def test_get_user_by_id(created_user, users_authenticated_api_client: UsersClient):
    user_id = created_user["id"]
    got = users_authenticated_api_client.get_user_by_id(user_id)
    assert got["id"] == user_id
    assert got["is_active"] is True