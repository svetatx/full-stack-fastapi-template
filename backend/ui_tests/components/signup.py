from playwright.sync_api import Page, expect
import re

def open_login(page: Page):
    page.goto("/login") 

def go_to_signup(page: Page):
    page.get_by_role("link", name="Sign Up").click()
    expect(page).to_have_url("/signup")

def register(page: Page, fullname: str, email: str, password: str):
    page.get_by_placeholder("Full Name").fill(fullname)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password", exact=True).fill(password)
    page.get_by_placeholder("Confirm Password").fill(password)
    page.get_by_role("button", name="Sign Up").click()

def assert_registered(page: Page):
    page.to_have_url("**/login")