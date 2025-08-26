from playwright.sync_api import Page

def login(page: Page, email: str, password: str):
    page.goto("/login")
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Log in").click()  
    page.to_have_url("**/dashboard")