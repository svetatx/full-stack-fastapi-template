import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/users"


# POST: создать пользователя
def post_user(email: str, password: str, full_name: str):
    payload = {
        "email": email,
        "password": password,
        "full_name": full_name
    }
    resp = requests.post(f"{BASE_URL}/signup", json=payload)
    print("POST USER:", resp.status_code, resp.json())
    return resp


# GET: получить список всех пользователей
def get_users():
    resp = requests.get(f"{BASE_URL}/")
    print("GET USERS:", resp.status_code, resp.json())
    return resp


# GET: получить конкретного пользователя по email
def get_user(email: str):
    resp = requests.get(f"{BASE_URL}/?email={email}")
    print("GET USER:", resp.status_code, resp.json())
    return resp


# DELETE: удалить пользователя по ID
def delete_user(user_id: int):
    resp = requests.delete(f"{BASE_URL}/{user_id}")
    print("DELETE USER:", resp.status_code)
    return resp
