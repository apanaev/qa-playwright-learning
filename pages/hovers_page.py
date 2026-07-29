from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement

class HoversPage(PageActions):

    def __init__(self,page:Page):
        super().__init__(page)
        self.avatar_locator = WebElement(page.locator("// img[ @ alt = 'User Avatar']"),"Аватар")
        self.user_name_locator= WebElement(page.locator("(//h5)[1]"), "Пользователь")

    def foo(self):
        self.avatar_locator.hover()

    def get_user(self):
        return self.user_name_locator.get_inner_text()





