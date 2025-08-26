
from playwright.sync_api import Page
from components import signup 


@pytest.fixture
def test_user(page: Page):
    email = "Test User"
    password = "StrongPass123!"
    fullname = "Test User"

    # регистрация через UI
    signup.open_login(page)
    signup.go_to_signup(page)
    signup.register(
        page,
        fullname=fullname,
        email=email,
        password=password
    )
    signup.assert_registered(page)

    return {"email": email, "password": password}