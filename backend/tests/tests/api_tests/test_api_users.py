from tests.api_tests.users import post_user, get_users, get_user

def test_create_user():
    email = "qa_user1@test.com"
    password = "Password123"
    full_name = "QA User 1"

    response = post_user(email, password, full_name)
    assert response.status_code == 200  

def test_get_all_users():
    response = get_users()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_email():
    email = "qa_user1@test.com"
    response = get_user(email)
    assert response.status_code == 200
    assert response.json()["email"] == email