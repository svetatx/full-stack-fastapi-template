import pytest
from random import randint
from faker import Faker
from playwright.sync_api import Page, Browser
from components import signup, login, delete_user
from pathlib import Path
import pytest
import allure
from pytest import TempPathFactory

BASE_URL = "http://localhost:5173"
fake = Faker()

@pytest.fixture
def page(browser: Browser):
    context = browser.new_context(base_url=BASE_URL)
    context.set_default_timeout(4000)
    page = context.new_page()
    yield page


@pytest.fixture
def signup_user(request, page: Page):
    fullname = fake.name()
    email = f"{randint(1, 100)}{fake.email()}"
    password = fake.password()

    login.open(page)
    signup.go_to_signup(page)
    signup.register(page, fullname=fullname, email=email, password=password)
    signup.assert_registered(page)

    yield {"fullname": fullname, "email": email, "password": password, "deleted": False}

    if not "no_user_cleanup" in request.keywords:
        delete_user.open_settings(page)
        delete_user.open_danger_zone(page)
        delete_user.delete_account(page)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, tmp_path_factory: TempPathFactory):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": tmp_path_factory.mktemp("videos/"),
        "record_video_size": {"width": 1920, "height": 1080},
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        if "page" in item.fixturenames:
            page: Page = item.funcargs["page"]

            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

            video_path = page.video.path()

            page.context.close()

            if video_path and Path(video_path).exists():
                with open(video_path, "rb") as video_file:
                    allure.attach(
                        video_file.read(),
                        name=f"video_{item.name}",
                        attachment_type=allure.attachment_type.WEBM,
                    )