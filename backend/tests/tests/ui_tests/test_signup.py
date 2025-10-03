import pytest
from playwright.sync_api import Page
from components import signup, login, items, delete_user
from faker import Faker

fake = Faker()

def test_user_can_register(page: Page):
    login.open(page)
    signup.go_to_signup(page)
    fullname = fake.name()
    email = fake.email()
    password = fake.password()
    signup.register(page, fullname=fullname, email=email, password=password)
    signup.assert_registered(page)

def test_login_with_test_user(page: Page, signup_user):
    login.as_user(page, signup_user["email"], signup_user["password"])
    # login.assert_logged_in(page)

def test_add_item(page: Page, signup_user):
    login.as_user(page, signup_user["email"], signup_user["password"])
    items.open_items_from_menu(page)
    items.open_add_modal(page)
    items.fill_item_form(page, title="title item", description=" ")
    items.save_item(page)
  