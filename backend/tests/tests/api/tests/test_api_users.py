from api.clients.users import register_user, get_user_by_id
from random import randint

def test_register_user():
    response = register_user(
    email = f"svetlana{randint(1, 1000)}@gmai.com",
    password = "Password123",
    full_name = "qa_user1",
    )
 
    assert response["is_active"] == True
    assert response["is_superuser"] == False


    
def test_get_user_by_id(created_user, auth_headers):
    user_id = created_user["id"]
    resp = get_user_by_id(user_id, headers=auth_headers)
    assert resp["id"] == user_id
    assert resp["is_active"] is True

    

