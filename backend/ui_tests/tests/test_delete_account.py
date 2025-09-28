from playwright.sync_api import Page
from components import delete_user, login
import pytest

@pytest.mark.no_user_cleanup
def test_delete_account(page: Page, signup_user):
    login.login(page, signup_user["email"], signup_user["password"])
    delete_user.open_settings(page)
    delete_user.open_danger_zone(page)
    delete_user.delete_account(page)

    # помечаем вручную, чтобы teardown не трогал
    signup_user["deleted"] = True