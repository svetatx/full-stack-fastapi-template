from playwright.sync_api import Page
from components import delete_user, user_setting


def test_update_user(page: Page, test_user):
    delete_user.open_settings(page)
    user_setting.open_my_profile(page)
    user_setting.edit_profile(page)
    user_setting.set_full_name(page, "testUser3")
    user_setting.save(page)
    user_setting.open_my_profile(page)
    user_setting.assert_full_name(page, "testUser3")