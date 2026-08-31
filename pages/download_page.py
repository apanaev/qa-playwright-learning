from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class DownloadPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.links_locator = MultiWebElement(page.locator("//*[@id='content']//*[@href]"), "Список ссылок")

    def get_link(self, index):
        return self.links_locator.nth(index)

    def get_link_text(self, index):
        return self.links_locator.nth(index).get_inner_text()
