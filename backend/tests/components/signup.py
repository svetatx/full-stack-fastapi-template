from playwright.sync_api import Page, expect


class SignUpForm:
    def __init__(self, page: Page):
        self.page = page

    def go_to_signup(self):
        self.page.get_by_role("link", name="Sign Up").click()
        expect(self.page).to_have_url("/signup")

    def register(self, fullname: str, email: str, password: str):
        self.page.get_by_placeholder("Full Name").fill(fullname)
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password", exact=True).fill(password)
        self.page.get_by_placeholder("Confirm Password").fill(password)
        self.page.get_by_role("button", name="Sign Up").click()

    def assert_registered(self):
        expect(self.page).to_have_url("/login")


        
