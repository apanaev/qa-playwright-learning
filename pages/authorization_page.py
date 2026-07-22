from playwright.sync_api import Page, Locator
from ui.page_actions import PageActions
from ui.web_element import WebElement


class AuthorizationPage(PageActions):
    def __init__(self, page:Page):
        super().__init__(page)
        self.success_message = WebElement(page.locator("//*[@id='content']//p"),"Сообщение об успешной авторизации")

    def get_success_message(self):
        return self.success_message.get_inner_text()
