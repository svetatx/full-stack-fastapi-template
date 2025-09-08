from components.login import LoginForm


def test_login(
    register_user_by_api, created_user, login: LoginForm, delete_user_by_api
):
    login.as_user(email=created_user.email, password=created_user.password)
