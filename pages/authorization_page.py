from playwright.sync_api import Page, Locator


class AuthorizationPage:
    def __init__(self, page):
        self.page = page
        self.success_message: Locator = page.locator("//*[@id='content']//p")

    def get_success_message(self):
        return self.success_message.inner_text()
