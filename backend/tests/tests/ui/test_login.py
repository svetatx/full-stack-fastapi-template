from playwright.sync_api import Page
from components import login


def test_login_with_test_user(page: Page,  signup_user):
    login.as_user(page, signup_user["email"], signup_user["password"])
    login.expect_logged_in(page)
