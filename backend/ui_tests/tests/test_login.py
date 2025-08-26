from playwright.sync_api import Page
from components import login 


def test_login_with_test_user(page: Page, test_user):
    login.open_login(page)
    login.login(
        page,
        email=test_user["email"],
        password=test_user["password"]
    )
    page.wait_for_url("**/dashboard")