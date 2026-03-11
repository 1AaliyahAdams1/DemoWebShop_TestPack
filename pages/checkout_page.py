from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from data.locators import *


class CheckoutPage(BasePage):

    # --- Actions ---
    def search_and_open_product(self, search_term):
        self.WaitFill(SearchBar_URL, search_term)
        self.WaitClick(SearchConfirm_URL)
        self.WaitClick(Item_URL)

    def add_to_cart(self):
        self.WaitClick(AddToCart_URL)
        expect(self.page.locator(AddToCartSuccess_URL)).to_be_visible(timeout=10_000)

    def open_cart(self):
        self.WaitClick(ShoppingCart_URL)

    def proceed_to_checkout(self):
        self.WaitClick(TermsOfService_URL)
        self.WaitClick(Checkout_URL)

    def fill_billing_address(self, country, city, address, zip_code, phone):
        self.page.wait_for_load_state("networkidle")
        billing_select = self.page.locator(BillingAddressSelect_URL)
        if billing_select.is_visible():
            billing_select.select_option(label="New Address")
        self.page.wait_for_selector(CountryDropDown_URL)
        self.page.select_option(CountryDropDown_URL, label=country)
        self.page.wait_for_load_state("networkidle")
        self.WaitFill(City_URL, city)
        self.WaitFill(Address1_URL, address)
        self.WaitFill(ZipCode_URL, zip_code)
        self.WaitFill(Phone_URL, phone)
        self.WaitClick(BillingAddressContinue_URL)

    def shipping_address(self):
        self.page.wait_for_load_state("networkidle")
        self.WaitClick(ShippingAddressContinue_URL)

    def shipping_method(self):
        self.page.wait_for_load_state("networkidle")
        self.WaitClick(ShippingMethodContinue_URL)

    def fill_payment_method(self):
        self.page.wait_for_load_state("networkidle")
        self.WaitClick(PaymentMethod_URL)
        self.WaitClick(PaymentMethodContinue_URL)

    def fill_payment_info(self, card_type, cardholder, card_number, expiry_month, expiry_year, cvv):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector(CardType_URL)
        self.page.select_option(CardType_URL, label=card_type)
        self.WaitFill(CardHolder_URL, cardholder)
        self.WaitFill(CardNumber_URL, card_number)
        self.page.select_option(ExpirationMonth_URL, value=expiry_month)
        self.page.select_option(ExpirationYear_URL, value=expiry_year)
        self.WaitFill(CardCode_URL, cvv)
        self.WaitClick(PaymentInformationContinue_URL)

    def confirm_order(self):
        self.page.wait_for_load_state("networkidle")
        self.WaitClick(ConfirmOrder_URL)

    # --- Assertions ---
    def assert_cart_contains(self, product_name, quantity = 0):
        CartItem = self.page.locator(CartItem_URL).inner_text()
        assert CartItem == product_name, f"Item not found in cart, got '{CartItem}'"
        Quantity = self.page.locator(CartQuantity_URL).input_value()
        assert int(Quantity) >= int(quantity), "Quantity incorrect/missing"
        print(CartItem, "found with quantity of", Quantity)

    def assert_order_confirmed(self):
        OrderConfirmation = self.page.locator(OrderConfirmation_URL).inner_text()
        assert OrderConfirmation == "Your order has been successfully processed!", "Order process failed"
        OrderNumber = self.page.locator(OrderNumber_URL).inner_text()
        print("Text:", OrderConfirmation, "found with", OrderNumber)