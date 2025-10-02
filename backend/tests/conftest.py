import pytest
from random import randint
from faker import Faker
from playwright.sync_api import Page, Browser
from components import signup, login, delete_user

BASE_URL = "http://localhost:5173"
fake = Faker()

@pytest.fixture
def page(browser: Browser):
    context = browser.new_context(base_url=BASE_URL)
    context.set_default_timeout(4000)
    page = context.new_page()
    yield page
    page.close()
    context.close()

@pytest.fixture
def signup_user(request, page: Page):
    fullname = fake.name()
    email = f"{randint(1, 100)}{fake.email()}"
    password = fake.password()

    login.open_login(page)
    signup.go_to_signup(page)
    signup.register(page, fullname=fullname, email=email, password=password)
    signup.assert_registered(page)

    yield {"fullname": fullname, "email": email, "password": password, "deleted": False}

    if not "no_user_cleanup" in request.keywords:
        delete_user.open_settings(page)
        delete_user.open_danger_zone(page)
        delete_user.delete_account(page)


    # user = {"fullname": fullname, "email": email, "password": password, "deleted": False}
    # yield user

    # # если тест сам удалял → пропускаем авто-очистку
    # if request.node.get_closest_marker("no_user_cleanup") or user.get("deleted"):
    #     return

    # # авто-удаление через UI (лучше через API, если есть)
    # try:
    #     delete_user.open_settings(page)
    #     delete_user.open_danger_zone(page)
    #     delete_user.delete_account(page)
    #     user["deleted"] = True
    # except Exception:
    #     # не ломаем весь ран, если в уборке что-то упало
    #     pass