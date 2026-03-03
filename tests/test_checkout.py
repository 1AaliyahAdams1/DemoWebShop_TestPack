from conftest import *

@pytest.mark.order(3)
def test_checkout(browser):
    page = browser.new_page()
    page.goto("https://demowebshop.tricentis.com/")

    #Login
    login(page)

    #Adding Item to Cart
    WaitFill(page, SearchBar_URL, Search_Term)
    WaitClick(page, SearchConfirm_URL)
    WaitClick(page, Item_URL)
    WaitClick(page, AddToCart_URL)
    WaitClick(page, ShoppingCart_URL)

    #Validate Shopping Cart
    Cartitem = page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div > div > div.page-body > div > form > table > tbody > tr > td.product > a").inner_text()
    assert Cartitem == "Digital SLR Camera - Black", "Item not found"

    Quantity = page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div > div > div.page-body > div > form > table > tbody > tr > td.qty.nobr > input").input_value()
    assert Quantity == '1', "Quantity incorrect/missing"

    print(Cartitem, "found with quantity of ", Quantity)

    #Checking out Shopping Cart
    WaitClick(page, TermsOfService_URL)
    WaitClick(page, Checkout_URL)

    #Billing Address
    WaitClick(page, CountryDropDown_URL)
    page.select_option(CountryDropDown_URL, value=Country)
    WaitFill(page, City_URL, City)
    WaitFill(page, Address1_URL, Address1)
    WaitFill(page, ZipCode_URL, ZipCode)
    WaitFill(page, Phone_URL, Phone)
    WaitClick(page, Continue_URL)

    #Shipping Address -> Shipping Method
    CounterWaitClick(page, Continue_URL)

    #Payment Method
    WaitClick(page, PaymentMethod_URL)
    page.locator(Continue_URL).nth(3).click()

    #Payment Information
    WaitFill(page, CardHolder_URL, CardHolder)
    WaitFill(page, CardNumber_URL, CardNumber)
    WaitClick(page, ExpirationDate_URL)
    page.select_option(ExpirationDate_URL, value= ExpiryMonth)
    #WaitClick(page, ExpirationYear_URL)
    #page.select_option(ExpirationYear_URL, value=ExpiryYear)
    WaitFill(page, CardCode_URL, Code)
    page.locator(Continue_URL).nth(4).click()

    #Confirm Order
    page.wait_for_selector(ConfirmOrder_URL)
    page.click(ConfirmOrder_URL)

    #Validate Confirm Order
    OrderNumber = page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div > div > div.page-body.checkout-data > div > ul > li:nth-child(1)").inner_text()
    OrderConfirmation = page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div > div > div.page-body.checkout-data > div > div.title > strong").inner_text()

    assert OrderConfirmation == "Your order has been successfully processed!", "Order process failed"

    print("Text:", OrderConfirmation ,"found with", OrderNumber)

    #Logout
    page.wait_for_selector(Logout_URL)
    page.click(Logout_URL)
