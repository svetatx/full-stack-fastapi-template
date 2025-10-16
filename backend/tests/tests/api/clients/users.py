from api.utils import api_request

BASE_URL = "http://127.0.0.1:8000"


# POST: создать пользователя
def register_user(email: str, password: str, full_name: str):
    return api_request(
        endpoint="/users/signup",
        method="POST",
        json={
            "email": email, 
            "password": password, 
            "full_name": full_name},
        expected_status=200
    )

def get_user_by_id(user_id: str):
    return api_request(
        endpoint="users/",
        method="Get",
        expected_status=200
    )