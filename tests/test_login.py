import pytest
from conftest import ensureCredentials
from pages.login_page import LoginPage


def test_login(page):
    email, password = ensureCredentials(page)

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(email, password)
    login_page.assert_logged_in(email)

    login_page.logout()
    login_page.assert_logged_out()