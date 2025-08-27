import pytest
from faker import Faker
from playwright.sync_api import Page
from components import signup, login

fake = Faker()

@pytest.fixture
def test_user(page: Page):
    fullname=fake.name()
    email=fake.email()
    password=fake.email()

    # регистрация через UI
    login.open_login(page)
    signup.go_to_signup(page)
    signup.register(
        page,
        fullname=fullname,
        email=email,
        password=password
    )
    signup.assert_registered(page)

    yield {"email": email, "password": password}