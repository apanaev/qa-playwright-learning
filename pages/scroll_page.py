from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[contains(@class, 'jscroll')]"), "Абзац")
        self.footer = page.locator("#page-footer")

    def scroll_down(self):
        count_para = self.count_paragraph()
        future_paragraph = self.scroll_locators.nth(self.count_paragraph())
        while count_para == self.count_paragraph():
            self.footer.scroll_into_view_if_needed()
        else:
            future_paragraph.wait_for_attached_state()

    def count_paragraph(self):
        return self.scroll_locators.count()
