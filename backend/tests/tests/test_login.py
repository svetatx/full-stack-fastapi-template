from components.login import LoginForm


def test_login(register_user, created_user, login: LoginForm):
    login.as_user(email=created_user.email, password=created_user.password)
