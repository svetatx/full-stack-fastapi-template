from playwright.sync_api import Page, expect


class LoginForm:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("/login")

    def as_user(self, email: str, password: str):
        self.open()
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Log in").click()
        expect(self.page).to_have_url("/")
