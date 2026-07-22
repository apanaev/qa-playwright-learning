from playwright.sync_api import Page, Locator
from ui.page_actions import PageActions
from ui.web_element import WebElement
class ContextMenuPage(PageActions):
    def __init__(self,page:Page):
        super().__init__(page)
        self.context_menu_locator = WebElement(page.locator("//div[@id='hot-spot']"),"Контекстное меню")


    def right_click_context_menu(self):
        self.context_menu_locator.right_click()
