import uuid
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
import pytest


# ---------------------------------------------------------------------------
# Credential Helpers
# ---------------------------------------------------------------------------
def generate_email() -> str:
    return f"testuser_{uuid.uuid4().hex[:8]}@example.com"


def makeCredentials(email, password):
    datafile = Path("Credentials.json")
    with open(datafile, "w") as json_file:
        json.dump({"email": email, "password": password}, json_file)
    print(f"Credentials saved: {email}")


def getCredentials():
    datafile = Path("Credentials.json")
    with open(datafile, "r") as read_file:
        file = json.load(read_file)
    return file["email"], file["password"]


def ensureCredentials(page):
    """
    Returns valid credentials.
    If Credentials.json doesn't exist, registers a new user first
    so each test can run independently without needing Part 1 to run first.
    """
    from data.test_data import First_Name, Last_Name, Password
    from pages.register_page import RegisterPage
    from pages.login_page import LoginPage

    datafile = Path("Credentials.json")
    if not datafile.exists():
        email = generate_email()
        register_page = RegisterPage(page)
        login_page = LoginPage(page)
        register_page.navigate()
        register_page.register(First_Name, Last_Name, email, Password)
        register_page.assert_registration_success()
        register_page.click_continue()
        login_page.logout()
        login_page.assert_logged_out()
        makeCredentials(email, Password)

    return getCredentials()


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page