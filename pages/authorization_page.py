from playwright.sync_api import Page, Locator
from pages.page_actions import PageActions

class AuthorizationPage(PageActions):
    def __init__(self, page:Page):
        super().__init__(page)
        self.success_message: Locator = page.locator("//*[@id='content']//p")

    def get_success_message(self):
        return self.success_message.inner_text()
