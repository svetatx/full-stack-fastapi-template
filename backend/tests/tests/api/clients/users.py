from api.tests.utils import api_request

BASE_URL = "http://127.0.0.1:8000"


# POST: создать пользователя
def register_user(email: str, password: str, full_name: str):
    return api_request(
        base_api_url=BASE_URL,
        endpoint="/signup",
        method="POST"
        json={
            "email": email, 
            "password": password, 
            "full_name": full_name},
    )
