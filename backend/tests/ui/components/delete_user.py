from playwright.sync_api import Page, expect

def open_settings(page: Page):
    page.locator('(//*[text()="User Settings"])[1]').click()
#     expect(page.get_by_role("heading", name="User Settings")).to_be_visible()

def open_danger_zone(page: Page):
     page.get_by_text("Danger zone").click()

def delete_account(page: Page):
     page.get_by_role("button", name="Delete").click()
     page.get_by_text("Confirmation Required")
     page.locator('(//*[text()="Delete"])[2]').click()

def login_page(page: Page):
    expect(page).to_have_url("http://localhost:5173/")