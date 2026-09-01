from playwright.sync_api import Page, expect

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[@class='jscroll-added']"), "Абзац")
        self.iterr = 0

    def scroll_down(self):
        self.iterr = self.iterr + 1
        last_paragraph = self.scroll_locators.nth(-1)
        last_paragraph.wait_for_load_state()
        last_paragraph.scroll_into_view_if_needed()

    def count_paragraf(self):
        return self.scroll_locators.count()
