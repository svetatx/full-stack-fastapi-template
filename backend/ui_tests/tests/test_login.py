from playwright.sync_api import Page
from components import login 


def test_login_with_test_user(page: Page, test_user):
    login.login(page, test_user["email"], test_user["password"])
    login.assert_logged_in(page)
