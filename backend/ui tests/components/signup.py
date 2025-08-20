from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:5173"

def open_login(page: Page):
    page.goto(f"{BASE_URL}/login")

def go_to_signup(page: Page):
    page.get_by_role("link", name="Sign Up").click()
    expect(page).to_have_url(f"{BASE_URL}/signup")

def register(page: Page, fullname: str, email: str, password: str):
    page.get_by_placeholder("Full Name").fill(fullname)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill(pasword)
    page.get_by_placeholder("Confirm Password").fill(password)
    page.get_by_role("button", name="Sign Up").click()

def assert_registered(page: Page):
    expect(page).to_have_url(f"{BASE_URL}/login")