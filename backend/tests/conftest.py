import pytest
from faker import Faker
from playwright.sync_api import Browser, Page
from pydantic import BaseModel
from components.login import LoginForm
from components.delete_user import DeleteUser
from components.signup import SignUpForm


# tammy76@example.com
# Heather Snow

# uv run pytest --headed --slowmo 300 


class User(BaseModel):
    fullname: str
    email: str
    password: str


@pytest.fixture(autouse=True)
def page(browser: Browser):
    context = browser.new_context(base_url="http://localhost:5173", viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture
def login(page: Page) -> LoginForm:
    return LoginForm(page)


@pytest.fixture
def signup(page: Page) -> SignUpForm:
    return SignUpForm(page)


@pytest.fixture
def delete_user(page: Page) -> DeleteUser:
    return DeleteUser(page)


@pytest.fixture
def created_user(faker: Faker) -> User:
    return User(fullname=faker.name(), email=faker.email(), password=faker.name())


@pytest.fixture
def register_user(
    created_user: User, signup: SignUpForm, login: LoginForm, delete_user: DeleteUser
):
    login.open()
    signup.go_to_signup()
    signup.register(
        fullname=created_user.fullname,
        email=created_user.email,
        password=created_user.password,
    )
    signup.assert_registered()

    yield

    delete_user.open_settings()
    delete_user.open_danger_zone()
    delete_user.delete_account()


@pytest.fixture
def authorize_user(login: LoginForm, signup: SignUpForm, created_user: User):
    login.open()
    login.as_user(created_user.email, created_user.password)
