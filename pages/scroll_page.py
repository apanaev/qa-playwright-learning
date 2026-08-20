from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[@class='jscroll-added']"), "Абзац")

    # def scroll_down(self):
    #     self.page.keyboard.press("End")
    #     self.page.wait_for_timeout(500)

    def scroll_down(self):
        a = self.scroll_locators.nth(-1)
        a.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)  ### да костыль, по другому у меня не получилось
