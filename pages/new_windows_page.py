from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class NewWindowsPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.text_locator = WebElement(self.page.locator("//h3"), "Текст нового окна")

    def get_text(self):
        return self.text_locator.get_inner_text()
