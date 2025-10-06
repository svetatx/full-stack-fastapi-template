import pytest
from random import randint
from faker import Faker
from playwright.sync_api import Page
from components import signup, login, delete_user
import pathlib
from playwright.sync_api import BrowserContext
import pytest
import allure

BASE_URL = "http://localhost:5173"
fake = Faker()

@pytest.fixture
def page(new_context: BrowserContext):
    context = new_context(base_url=BASE_URL)
    context.set_default_timeout(4000)
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    yield

    try:
        artifacts_dir = item.funcargs.get("output_path")

        if artifacts_dir:
            artifacts_dir_path = pathlib.Path(artifacts_dir)

            if artifacts_dir_path.is_dir():
                for file in artifacts_dir_path.iterdir():
                    if file.is_file() and file.suffix == ".webm":
                        allure.attach.file(
                            file,
                            name=file.name,
                            attachment_type=allure.attachment_type.WEBM,
                        )

    except Exception as e:
        print(f"Error attaching video: {e}")