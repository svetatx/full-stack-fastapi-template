from playwright.sync_api import Page
from components import delete_user, user_setting, login, signup
from faker import Faker
fake = Faker()

def test_user_can_register(page: Page):
    login.open_login(page)
    signup.go_to_signup(page)
    fullname = fake.name()
    email = fake.email() 
    password = fake.password()
    signup.register(page, fullname=fullname, email=email, password=password)
    signup.assert_registered(page)

def test_login_with_test_user(page: Page, signup_user):
    login.login(page, signup_user["email"], signup_user["password"])

def test_update_user(page: Page, signup_user):
    login.login(page, signup_user["email"], signup_user["password"])
    delete_user.open_settings(page)
    user_setting.open_my_profile(page)
    user_setting.edit_profile(page)
    user_setting.set_full_name(page, "testUser3")
    user_setting.save(page)
    user_setting.assert_update_success(page)
    user_setting.open_my_profile(page)