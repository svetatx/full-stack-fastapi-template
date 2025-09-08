from playwright.sync_api import Page, expect
from allure import step


class LoginForm:
    def __init__(self, page: Page):
        self.page = page

    @step("Open login form")
    def open(self):
        self.page.goto("/login")

    @step("Login as user")
    def as_user(self, email: str, password: str):
        self.open()
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Log in").click()
        expect(self.page).to_have_url("/")
