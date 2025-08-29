import pytest
from faker import Faker
from playwright.sync_api import Page
from components import signup, login,delete_user, items
BASE_URL = "http://localhost:5173"
fake = Faker()
 
@pytest.fixture
def page_baseurl(browser: Browser):
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    yield page
    page.close()
    context.close()
    
@pytest.fixture
def sugnup_user(page: Page):
    fullname=fake.name()
    email=fake.email()
    password=fake.email()
    login.open_login(page)
    signup.go_to_signup(page)
    signup.register(
        page,
        fullname=fullname,
        email=email,
        password=password
    )
    signup.assert_registered(page)

    yield {"fullname": fullname, "email": email, "password": password}

    delete_user.open_settings(page)
    delete_user.open_danger_zone(page)
    delete_user.delete_account(page)