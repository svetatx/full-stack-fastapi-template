from playwright.sync_api import Page
from components import signup, login
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