from pages.new_windows_page import NewWindowsPage
from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class WindowsPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.windows_locator = WebElement(page.locator("//a[@href='/windows/new']"), "Click Here")

    def open_new_window(self):
        new_page = self.expect_new_page(self.windows_locator.click)
        return NewWindowsPage(new_page)
