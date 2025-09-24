from playwright.sync_api import Page
from components import items, login

def test_add_item(page: Page, ):
    login.login(page, ["email"], test_user["password"])
    items.open_items_from_menu(page)
    items.open_add_modal(page)
    items.fill_item_form(page, title="title item", description=" ")
    items.save_item(page)
    items.open_row_menu(page)
    items.delete_item(page)
