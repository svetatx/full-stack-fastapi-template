from playwright.sync_api import Page
from components import login 


def test_login_with_test_user(page: Page, signup_user):
    login.login(page, signup_user["email"], signup_user["password"])
    login.assert_logged_in(page)