import pytest
from components.delete_user import DeleteUser
from components.login import LoginForm
from components.signup import SignUpForm
from faker import Faker
import allure
from typing import Generator, Any
from allure_commons.reporter import AllureReporter
from allure_pytest.listener import AllureListener
from playwright.sync_api import Browser, Page
from testing.utils.client import Client
from testing.utils.configuration import Configuration
from clients.users import UsersClient, UserRegister
from clients.login import LoginClient, UserAccessToken


# tammy76@example.com
# Heather Snow

# uv run pytest --headed --slowmo 300


# API
@pytest.fixture
def unauth_configuration():
    return Configuration(
        base_url="http://127.0.0.1:8000",
        # headers={"Authorization": f"Bearer {API_KEY}"},
    )


@pytest.fixture
def unauth_client(unauth_configuration):
    return Client(configuration=unauth_configuration)


@pytest.fixture
def login_client(unauth_client) -> LoginClient:
    return LoginClient(unauth_client)


@pytest.fixture
def unauth_users_client(unauth_client: Client) -> UsersClient:
    return UsersClient(unauth_client)


@pytest.fixture
def created_user(faker: Faker) -> UserRegister:
    return UserRegister(
        fullname=faker.name(), email=faker.email(), password=faker.name()
    )


@pytest.fixture
def register_user_by_api(
    faker: Faker,
    unauth_users_client: UsersClient,
    created_user: UserRegister,
):
    unauth_users_client.register_user(
        UserRegister(
            fullname=created_user.fullname,
            email=created_user.email,
            password=created_user.password,
        )
    )


@pytest.fixture
def get_access_token(
    login_client: LoginClient, created_user, register_user_by_api
) -> dict:
    return login_client.get_access_token(
        user=UserAccessToken(
            username=created_user.email, password=created_user.password
        )
    ).json()


@pytest.fixture
def auth_configuration(get_access_token):
    return Configuration(
        base_url="http://127.0.0.1:8000",
        headers={"Authorization": f"Bearer {get_access_token['access_token']}"},
    )


@pytest.fixture
def auth_client(auth_configuration):
    return Client(configuration=auth_configuration)


@pytest.fixture
def auth_users_client(auth_client) -> UsersClient:
    return UsersClient(auth_client)


@pytest.fixture
def delete_user_by_api(auth_users_client: UsersClient):
    yield
    auth_users_client.delete_me()


# UI


@pytest.fixture(autouse=True)
def page(browser: Browser):
    context = browser.new_context(
        base_url="http://localhost:5173", viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()

    yield page

    page.close()
    context.close()


@pytest.fixture(scope="function", autouse=True)
def add_screenshot(page: Page, request: pytest.FixtureRequest):
    yield

    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=f"screenshot_{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )


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
def register_user_by_ui(
    created_user: UserRegister,
    signup: SignUpForm,
    login: LoginForm,
    delete_user: DeleteUser,
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
def authorize_user_by_ui(
    login: LoginForm, signup: SignUpForm, created_user: UserRegister
):
    login.open()
    login.as_user(created_user.email, created_user.password)


def allure_logger(config: pytest.Config) -> AllureReporter:
    listener: AllureListener = config.pluginmanager.get_plugin("allure_listener")
    return listener.allure_logger


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_fixture_setup(
    fixturedef, request: pytest.FixtureRequest
) -> Generator[None, Any, None]:
    yield
    logger: AllureReporter = allure_logger(request.config)
    item: pytest.Item = logger.get_last_item()
    scope_letter = fixturedef.scope[0].upper()
    item.name = f"[{scope_letter}] " + " ".join(fixturedef.argname.split("_")).title()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> None:
    if call.when == "call":
        test_name = item.name.replace("test_", "").replace("_", " ").capitalize()
        allure.dynamic.title(test_name)
