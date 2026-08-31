from playwright.sync_api import Page, expect

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[@class='jscroll-added']"), "Абзац")

    def scroll_down(self):
        count = self.scroll_locators.count()
        last_paragraph = self.scroll_locators.nth(-1)
        last_paragraph.scroll_into_view_if_needed()
        try:  # сделал блок try expect, без него одной прокрутки scroll_into_view_if_needed не хватает
            expect(self.scroll_locators.locator).not_to_have_count(count)
        except AssertionError:  # заметил что чаще срабатывает этот блок, но почему понять не могу.
            # вообще если использовать нажатие кнопки End, а не scroll_into_view_if_needed
            # то тест проходит быстрее или если использовать явное ожидание
            last_paragraph = self.scroll_locators.nth(-1)
            last_paragraph.scroll_into_view_if_needed()
            expect(self.scroll_locators.locator).not_to_have_count(count)
