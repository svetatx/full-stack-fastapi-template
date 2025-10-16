from api.clients.users import register_user
from random import randint

def test_register_user():
    response = register_user(
    email = f"svetlana{randint(1, 1000)}@gmai.com",
    password = "Password123",
    full_name = "qa_user1",
    )
 
    assert response["is_active"] == True
    assert response["is_superuser"] == False