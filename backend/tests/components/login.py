from playwright.sync_api import Page, expect

def open_login(page: Page):
    page.goto("/")

def login(page: Page, email: str, password: str):  
    open_login(page)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Log in").click()  

def expect_logged_in(page: Page):
    expect(page).to_have_url("/")