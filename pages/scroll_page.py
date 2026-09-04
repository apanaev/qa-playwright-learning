from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(
            page.locator("//div[contains(@class, 'jscroll') and contains(@class, 'added') "
                         "and normalize-space(text()) != '']"), "Абзац")

    def scroll_down(self):
        count = self.count_paragraph()
        next_paragraph = self.scroll_locators.nth(count)

        last_paragraph = self.scroll_locators.nth(-1)
        last_paragraph.scroll_into_view_if_needed()

        next_paragraph.wait_for_attached_state()

    def count_paragraph(self):
        return self.scroll_locators.count()
