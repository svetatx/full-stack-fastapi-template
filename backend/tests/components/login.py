from playwright.sync_api import Page, expect

def open_login(page: Page):
    page.goto("http://localhost:5173/")

def login(page: Page, email: str, password: str):  
    open_login(page)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Log in").click()  
    expect(page).to_have_url("http://localhost:5173/")