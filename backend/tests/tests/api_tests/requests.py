import requests

BASE_URL = "http://127.0.0.1:8000"

# Create user
playload = {
  {
  "email": "user@example.com",
  "password": "stringst",
  "full_name": "string"
}
}
resp = requests.post(f"{BASE_URL}/api/v1/users/signup", json=playload)
print("CREATE:", resp.status_code, resp.json())
# save email
created_email = playload["email"]

# 2. Get user
resp = requests.get(f"{BASE_URL}/api/v1/users/")
print("GET USERS:", resp.status_code, resp.json())

# # 3. Delete users
# if user_id:
#     resp = requests.delete(f"{BASE_URL}/api/v1/users/{user_id}")
#     print("DELETE:", resp.status_code, resp.text)

# def test_get_users():
#     resp = requests.get(f"{BASE_URL}/users?")
#     assert resp.status_code == 200
#     data = resp.json()


# def test_create_user():
#     new_user = {"name": "morpheus", "job": "leader"}
#     resp = requests.post(f"{BASE_URL}/users", json=new_user)
#     assert resp.status_code == 201
#     body = resp.json()
#     assert body["name"] == "morpheus"