from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class DownloadPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.links_locator = WebElement(page.locator("//*[@id='content']"),"Список ссылок")


