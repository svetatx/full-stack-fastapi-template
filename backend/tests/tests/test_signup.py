# from components import delete_user, items, login, signup
# from faker import Faker
# from playwright.sync_api import Page

# fake = Faker()


# def test_user_can_register(page: Page):
#     login.open_login(page)
#     signup.go_to_signup(page)
#     fullname = fake.name()
#     email = fake.email()
#     password = fake.password()
#     signup.register(page, fullname=fullname, email=email, password=password)
#     signup.assert_registered(page)


# def test_login_with_test_user(page: Page, test_user):
#     login.login(page, test_user["email"], test_user["password"])
#     login.assert_logged_in(page)


# def test_add_item(page: Page, test_user):
#     login.login(page, test_user["email"], test_user["password"])
#     items.open_items_from_menu(page)
#     items.open_add_modal(page)
#     items.fill_item_form(page, title="title item", description=" ")
#     items.save_item(page)


# def test_delete_account(page: Page, test_user):
#     delete_user.open_settings(page)
#     delete_user.open_danger_zone(page)
#     delete_user.delete_account(page)
