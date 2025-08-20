import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page_context(page: Page):

    yield page