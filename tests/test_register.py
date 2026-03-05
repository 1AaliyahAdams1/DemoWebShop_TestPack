from conftest import *
import json

New_Email = ""
Password = "Tosca1234!"

@pytest.mark.order(1)
def test_register(browser):
    page = browser.new_page()
    page.goto("https://demowebshop.tricentis.com/")

    #Redirecting to register page
    WaitClick(page, Register_URL)

    #Filling the details
    WaitClick(page, Gender_URL)
    WaitFill(page, FName_URL, First_Name)
    WaitFill(page, LName_URL, Last_Name)

    New_Email = GenerateEmail()

    WaitFill(page, Email_URL, New_Email)
    WaitFill(page, Password_URL, Password)
    WaitFill(page, CPassword_URL, Password)
    WaitClick(page, Register2_URL)

    #Checks that page has a success message for registration
    ValidationText = page.locator(RegistrationMessage_URL).inner_text()
    assert ValidationText == "Your registration completed", "Registration failed"
    print("Text:", ValidationText, "found")

    #Clicks confirm button
    WaitClick(page, Confirm_URL)

    #Logs the user out
    WaitClick(page, Logout_URL)

    #Saves credentials into a json file
    makeCredentials(New_Email, Password)