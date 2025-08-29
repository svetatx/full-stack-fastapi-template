from playwright.sync_api import Page, expect

def open_settings(page: Page):
    page.get_by_role("link", name="User Settings").click()
    expect(page.get_by_role("heading", name="User Settings")).to_be_visible()

def open_denger_zone(page: Page):
     page.get_by_role("link", name="Danger zone").click()

def delete_acount(page: Page):
     page.get_by_role("button", name="Delete").click()
     modal = page.get_by_role("dialog", name="Confirmation Required")
     expect(modal).to_be_visible()
     modal.get_by_role("button", name="Delete").click()

def login_page(page: Page):
    expect(page).to_have_url("http://localhost:5173/login")
     
