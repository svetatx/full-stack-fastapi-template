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

    
def test_get_user_by_id():
    user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" 
    response =  get_user_by_id(user_id)

    assert response["id"] == user_id
    assert response["is_active"] == True
    

