import pytest
from conftest import generate_email, makeCredentials
from data.test_data import First_Name, Last_Name, Password
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


def test_register(page):
    register_page = RegisterPage(page)
    login_page    = LoginPage(page)

    email = generate_email()

    register_page.navigate()
    register_page.register(First_Name, Last_Name, email, Password)
    register_page.assert_registration_success()
    register_page.click_continue()

    login_page.logout()
    login_page.assert_logged_out()

    makeCredentials(email, Password)