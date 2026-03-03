from conftest import *

@pytest.mark.order(2)
def test_login(browser):
    page = browser.new_page()
    page.goto("https://demowebshop.tricentis.com/")

    login(page)

    #Validates that the user is logged in
    ValidationText = page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.header-links-wrapper > div.header-links > ul > li:nth-child(1) > a").inner_text()

    email, password = getCredentials()

    assert ValidationText == email, "Login failed"
    print("Text:", ValidationText, "found")

    #Logs the user out
    WaitClick(page, Logout_URL)
