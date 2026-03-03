import random
from playwright.sync_api import sync_playwright, expect
import pytest
import json
from pathlib import Path

#Global Variables
First_Name = "Barbara"
Last_Name = "Gordon"
Search_Term = "Digital SLR Camera"
Country = "Austria"
City = "Vienna"
Address1 = "Vienna Street"
ZipCode = "1234"
Phone = "001122334455"

CardType = "Visa"
CardHolder = "Barbara Gordon"
CardNumber = "4485564059489345"
ExpiryMonth = "04"
ExpiryYear = "2022"
Code = "123"

#XPaths
Login_URL = "//a[text()='Log in']"
Email_URL = "//input[@id='Email']"
Password_URL = "//input[@id='Password']"
Login2_URL = "//input[@value = 'Log in']"
Logout_URL = "//a[text()='Log out']"

Register_URL = "//a[text()='Register']"
Gender_URL = "//input[@id='gender-female']"
FName_URL = "//input[@id='FirstName']"
LName_URL = "//input[@id='LastName']"
CPassword_URL = "//input[@id='ConfirmPassword']"
Register2_URL = "//input[@id='register-button']"
Confirm_URL = "//input[@value='Continue']"

SearchBar_URL = "//input[@id='small-searchterms']"
SearchConfirm_URL = "body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.search-box > form > input.button-1.search-box-button"
Item_URL = "body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div > div.page-body > div.search-results > div.product-grid > div > div > div.details > h2 > a"
AddToCart_URL = "//input[@id='add-to-cart-button-18']"
ShoppingCart_URL = "//span[text()='Shopping cart']"
TermsOfService_URL = "//input[@id='termsofservice']"
Checkout_URL = "//button[@id='checkout']"
CountryDropDown_URL = "//select[@id='BillingNewAddress_CountryId']"
CountryOption_URL = "//option[@value='1']"
City_URL = "//input[@id='BillingNewAddress_City']"
Address1_URL = "//input[@id='BillingNewAddress_Address1']"
Address2_URL = "//input[@id='BillingNewAddress_Address2']"
ZipCode_URL = "//input[@id='BillingNewAddress_ZipPostalCode']"
Phone_URL = "//input[@id='BillingNewAddress_PhoneNumber']"
Fax_URL = "//input[@id='BillingNewAddress_FaxNumber']"
Continue_URL = "//input[@value='Continue']"
ConfirmOrder_URL = "//input[@value='Confirm']"

PaymentMethod_URL = '//input[@id="paymentmethod_2"]'
CardHolder_URL = '//input[@id="CardholderName"]'
CardNumber_URL = '//input[@id="CardNumber"]'
ExpirationDate_URL = '//select[@id="ExpireMonth"]'
ExpirationYear_URL = '//select[@id="ExpireYear"]'
CardCode_URL = '//input[@id="CardCode"]'


@pytest.fixture
def browser():
    #Opens the browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def login(page):
    #Grabs Credentials from json file
    email, password = getCredentials()

    #Clicks and navigates to login page
    WaitClick(page, Login_URL)

    #Fills in details
    WaitFill(page, Email_URL, email)
    WaitFill(page, Password_URL, password)
    WaitClick(page, Login2_URL)

def makeCredentials(email, password):
    #Creates and save credentails into json file
    datafile = Path("Credentials.json")
    with open(datafile, "w") as json_file:
        json.dump({
            "email": email,
            "password": password,
        }, json_file)

def getCredentials():
    #Reads credentials from json file
    datafile = Path("Credentials.json")
    with open(datafile, "r") as read_file:
        file = json.load(read_file)
        Email = file["email"]
        Password = file["password"]
    return Email, Password

def GenerateEmail():
    #generates unique random email
    randNum = random.randint(1, 10)
    randWord = "Test"
    for i in range(randNum):
        randWord += random.choice(
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"])
    New_Email = f"0{randWord}0{randNum}0{randWord}0{randNum}0@gmail.com"

    return New_Email

def WaitClick(page, url):
    # waits for a selector before clicking
    page.wait_for_selector(url)
    page.click(url)

def WaitFill(page, url, text):
    # waits for a selector before filling it in
    page.wait_for_selector(url)
    page.fill(url, text)

def CounterWaitClick(page, url):
    # loop to wait for and click each continue button that appears on the checkout page
    # Ensures that the counter increments so that it uses the next continue button
    for i in range(2):
        i += 1
        page.locator(url).nth(i).click()
