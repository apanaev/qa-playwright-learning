from playwright.sync_api import Page, Locator

class ContextMenuPage:
    def __init__(self,page:Page):
        self.page = page
        self.context_menu_locator:Locator= page.locator("//div[@id='hot-spot']")


    def right_click_context_menu(self):
        self.context_menu_locator.click(button="right")
