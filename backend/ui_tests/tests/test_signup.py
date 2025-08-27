from playwright.sync_api import Page
from components import signup, login
from faker import Faker
fake = Faker()

def test_user_can_register(page: Page):
    login.open_login(page)
    # Step 2: нажать Sign Up
    signup.go_to_signup(page)
    # Step 3: fill registration
    signup.register(page,
        fullname="Test User",
        email= fake.unique.email(),
        password="StrongPass123!"
    )
    # Step 4: check succesfull registartion
    signup.assert_registered(page)