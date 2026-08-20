from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement


class HoversPage(PageActions):

    def __init__(self, page: Page):
        super().__init__(page)
        self.avatar_locator = MultiWebElement(page.locator("// img[ @ alt = 'User Avatar']"), "Аватар")
        self.user_name_locator = MultiWebElement(page.locator("(//h5)"), "Пользователь")

    def get_user(self, index):
        return self.user_name_locator.nth(index).get_inner_text()
