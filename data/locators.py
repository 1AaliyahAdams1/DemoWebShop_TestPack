# --- Navigation ---
Login_URL    = "//a[text()='Log in']"
Logout_URL   = "//a[text()='Log out']"
Register_URL = "//a[text()='Register']"

# --- Login page ---
Email_URL    = "//input[@id='Email']"
Password_URL = "//input[@id='Password']"
Login2_URL   = "//input[@value='Log in']"

# --- Registration page ---
Gender_URL    = "//input[@id='gender-female']"
FName_URL     = "//input[@id='FirstName']"
LName_URL     = "//input[@id='LastName']"
CPassword_URL = "//input[@id='ConfirmPassword']"
Register2_URL = "//input[@id='register-button']"
Confirm_URL   = "//input[@value='Continue']"

# --- Header validation ---
LoginMessage_URL        = "//div[@class='header']//a[@class='account']"
RegistrationMessage_URL = "//div[@class='result']"

# --- Product / Search ---
SearchBar_URL        = "//input[@id='small-searchterms']"
SearchConfirm_URL    = "//input[@type='submit'][@value='Search']"
Item_URL             = "//a[contains(text(),'Digital SLR Camera')]"
AddToCart_URL        = "//input[@id='add-to-cart-button-18']"
AddToCartSuccess_URL = "//div[@class='bar-notification success']"

# --- Cart ---
ShoppingCart_URL = "//span[text()='Shopping cart']"
CartItem_URL     = "//table[@class='cart']//tr[@class='cart-item-row']//td[@class='product']//a"
CartQuantity_URL = "//table[@class='cart']//tr[@class='cart-item-row']//td[@class='qty nobr']//input"

# --- Checkout ---
TermsOfService_URL       = "//input[@id='termsofservice']"
Checkout_URL             = "//button[@id='checkout']"
BillingAddressSelect_URL = "#billing-address-select"
CountryDropDown_URL      = "//select[@id='BillingNewAddress_CountryId']"
City_URL                 = "//input[@id='BillingNewAddress_City']"
Address1_URL             = "//input[@id='BillingNewAddress_Address1']"
ZipCode_URL              = "//input[@id='BillingNewAddress_ZipPostalCode']"
Phone_URL                = "//input[@id='BillingNewAddress_PhoneNumber']"
BillingAddressContinue_URL = "//div[@id='checkout-step-billing']//input[@value='Continue']"
ShippingAddressContinue_URL = "//div[@id='checkout-step-shipping']//input[@title='Continue']"
ShippingMethodContinue_URL = "//div[@id='checkout-step-shipping-method']//input[@value='Continue']"
PaymentMethodContinue_URL = "//div[@id='checkout-step-payment-method']//input[@value='Continue']"
PaymentInformationContinue_URL = "//div[@id='checkout-step-payment-info']//input[@value='Continue']"
ConfirmOrder_URL =  "//div[@id='checkout-step-confirm-order']//input[@value='Confirm']"

# --- Payment ---
PaymentMethod_URL   = "//input[@id='paymentmethod_2']"
CardType_URL        = "//select[@id='CreditCardType']"
CardHolder_URL      = "//input[@id='CardholderName']"
CardNumber_URL      = "//input[@id='CardNumber']"
ExpirationMonth_URL = "//select[@id='ExpireMonth']"
ExpirationYear_URL  = "//select[@id='ExpireYear']"
CardCode_URL        = "//input[@id='CardCode']"

# --- Order confirmation ---
OrderConfirmation_URL = "//div[@class='page checkout-page']//div[@class='title']"
OrderNumber_URL       = "//div[@class='page checkout-page']//li[contains(text(),'Order number')]"