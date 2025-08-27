from playwright.sync_api import Page, expect

def go_to_signup(page: Page):
    page.get_by_role("link", name="Sign Up").click()
    expect(page).to_have_url("http://localhost:5173/signup")

def register(page: Page, fullname: str, email: str, password: str):
    page.get_by_placeholder("Full Name").fill(fullname)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password", exact=True).fill(password)
    page.get_by_placeholder("Confirm Password").fill(password)
    page.get_by_role("button", name="Sign Up").click()

def assert_registered(page: Page):
    expect(page).to_have_url("http://localhost:5173/login")