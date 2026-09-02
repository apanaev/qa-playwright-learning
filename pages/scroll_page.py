from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[contains(@class, 'jscroll') "
                                                            "and contains(@class, 'added')]"), "Абзац")
        self.footer = page.locator("#page-footer")

    def scroll_down(self):
        next_paragraph = self.scroll_locators.nth(self.count_paragraph())
        self.footer.scroll_into_view_if_needed()
        self.footer.wait_for(state="visible")
        print("1")

        next_paragraph.locator.wait_for(state="visible")

    def count_paragraph(self):
        return self.scroll_locators.count()
