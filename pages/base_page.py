from playwright.sync_api import Page

class BasePage:
    BASE_URL = "https://demowebshop.tricentis.com"

    def __init__(self, page: Page):
        self.page = page

    def WaitClick(self, url):
        self.page.wait_for_selector(url)
        self.page.click(url)

    def WaitFill(self, url, text):
        self.page.wait_for_selector(url)
        self.page.fill(url, text)