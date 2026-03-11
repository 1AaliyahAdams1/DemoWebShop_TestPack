from playwright.sync_api import Page
from data.locators import (
    Register_URL, Gender_URL, FName_URL, LName_URL,
    Email_URL, Password_URL, CPassword_URL, Register2_URL,
    Confirm_URL, RegistrationMessage_URL
)
from pages.base_page import BasePage


class RegisterPage(BasePage):

    # --- Actions ---
    def navigate(self):
        self.page.goto(self.BASE_URL)
        self.WaitClick(Register_URL)

    def register(self, first_name, last_name, email, password):
        self.WaitClick(Gender_URL)
        self.WaitFill(FName_URL, first_name)
        self.WaitFill(LName_URL, last_name)
        self.WaitFill(Email_URL, email)
        self.WaitFill(Password_URL, password)
        self.WaitFill(CPassword_URL, password)
        self.WaitClick(Register2_URL)

    def click_continue(self):
        self.WaitClick(Confirm_URL)

    # --- Assertions ---
    def assert_registration_success(self):
        ValidationText = self.page.locator(RegistrationMessage_URL).inner_text()
        assert ValidationText == "Your registration completed", "Registration failed"
        print("Text:", ValidationText, "found")