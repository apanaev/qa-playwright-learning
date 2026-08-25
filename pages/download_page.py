from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class DownloadPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.links_locator = MultiWebElement(page.locator("//*[@id='content']//*[@href]"),"Список ссылок")


    def get_text_third_link_and_text(self):
        third_link = self.links_locator.nth(2)
        return third_link.get_inner_text(), third_link

