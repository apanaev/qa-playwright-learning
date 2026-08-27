from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class WindowsPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.windows_locator = WebElement(page.locator("//a[@href='/windows/new']"), "Click Here")

    def open_new_window_and_get_text(self):
        new_page = self.expect_new_page(self.windows_locator.click)
        new_page_text = WebElement(new_page.locator("//h3"), "Текст нового окна").get_inner_text()
        return new_page, new_page_text
