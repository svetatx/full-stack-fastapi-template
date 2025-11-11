from playwright.sync_api import Page, expect


def open_items_from_menu(page: Page):
    page.get_by_role("link", name="Items").click()
    expect(page.get_by_role("heading", name="Items Management")).to_be_visible()

def open_add_modal(page : Page):
    page.get_by_role("button", name="Add Item").click()
    expect(page.get_by_role("heading", name="Add Item")).to_be_visible()

def fill_item_form(page: Page, title: str, description: str = ""):
    page.get_by_placeholder("Title").fill(title)
    page.get_by_placeholder("Description").fill(description)

def save_item(page: Page):
    page.get_by_role("button", name="Save").click()

def expect_title_required_error(page: Page):
    expect(page.get_by_text("Title is required.")).to_be_visible()

def expect_item_visible(page: Page, title: str):
    expect(page.get_by_text(title)).to_be_visible()

def open_row_menu(page: Page):
    page.locator('button[data-scope="menu"][data-part="trigger"]').click()
    expect(page.get_by_role("menu")).to_be_visible()

def delete_item(page: Page):
    page.get_by_role("menu", name="Delete item").click()