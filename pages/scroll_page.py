from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page,expect



class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[@class='jscroll-added']"), "Абзац")

    def scroll_down(self):

        count = self.scroll_locators.count()

        last_paragraph = self.scroll_locators.nth(-1)
        last_paragraph.scroll_into_view_if_needed()

        expect(self.scroll_locators.locator).not_to_have_count(count)


