from playwright.sync_api import Page, expect


class DeleteUser:
    def __init__(self, page: Page):
        self.page = page

    def open_settings(self):
        self.page.get_by_role("link", name="User Settings").click()
        expect(self.page.get_by_role("heading", name="User Settings")).to_be_visible()

    def open_danger_zone(self):
        self.page.locator('//*[text()="Danger zone"]').click()

    def delete_account(self):
        self.page.get_by_role("button", name="Delete").click()
        expect(self.page.locator('//*[text()="Confirmation Required"]')).to_be_visible()
        self.page.locator('(//*[text()="Delete"])[2]').click()
        

    def login_page(self):
        expect(page).to_have_url("/login")
