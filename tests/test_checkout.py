import pytest
from conftest import ensureCredentials
from data.test_data import *
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def test_checkout(page):
    email, password = ensureCredentials(page)

    login_page    = LoginPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.navigate()
    login_page.login(email, password)
    login_page.assert_logged_in(email)

    # Add item to cart
    checkout_page.search_and_open_product(Search_Term)
    checkout_page.add_to_cart()
    checkout_page.open_cart()

    # Validate cart
    checkout_page.assert_cart_contains(Product_Name)

    # Checkout
    checkout_page.proceed_to_checkout()
    checkout_page.fill_billing_address(Country, City, Address1, ZipCode, Phone)
    checkout_page.shipping_address()
    checkout_page.shipping_method()
    checkout_page.fill_payment_method()
    checkout_page.fill_payment_info(CardType, CardHolder, CardNumber, ExpiryMonth, ExpiryYear, Code)
    checkout_page.confirm_order()
    checkout_page.assert_order_confirmed()

    # Logout
    login_page.logout()
    login_page.assert_logged_out()