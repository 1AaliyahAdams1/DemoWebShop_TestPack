from playwright.sync_api import Page, expect
from data.locators import (
    Login_URL, Email_URL, Password_URL, Login2_URL,
    Logout_URL, LoginMessage_URL
)
from pages.base_page import BasePage


class LoginPage(BasePage):

    # --- Actions ---
    def navigate(self):
        self.page.goto(self.BASE_URL)

    def login(self, email, password):
        self.WaitClick(Login_URL)
        self.WaitFill(Email_URL, email)
        self.WaitFill(Password_URL, password)
        self.WaitClick(Login2_URL)

    def logout(self):
        self.WaitClick(Logout_URL)

    # --- Assertions ---
    def assert_logged_in(self, email):
        ValidationText = self.page.locator(LoginMessage_URL).inner_text()
        assert ValidationText == email, "Login failed"
        print("Text:", ValidationText, "found")

    def assert_logged_out(self):
        self.page.wait_for_selector(Login_URL)
        expect(self.page.locator(Login_URL)).to_be_visible()