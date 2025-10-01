from playwright.sync_api import Page, expect

def open_my_profile(page: Page):
    page.get_by_role("tab", name="My profile").click()
    expect(page.get_by_role("tabpanel")).to_be_visible()

def edit_profile(page: Page):
    page.get_by_role("button", name="Edit").click()
    expect(page.get_by_label("Full name")).to_be_enabled()

def set_full_name(page: Page, value: str):
    page.get_by_label("Full name").fill(value)

def set_email(page: Page, value: str):
    page.get_by_label("Email").fill(value)

def save(page: Page):
    page.get_by_role("button", name="Save").click()

def assert_update_success(page):
    expect(page.get_by_text("User updated successfully")).to_be_visible()