from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class ScrollPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_locators = MultiWebElement(page.locator("//div[contains(@class, 'jscroll') "
                                                            "and contains(@class, 'added')]"), "Абзац")
        self.footer = page.locator("#page-footer")

        self.a = 0

    def scroll_down(self):
        self.a = self.a + 1
        # self.footer.wait_for(state="attached")
        # next_paragraph = self.scroll_locators.nth(self.count_paragraph())
        # self.footer.scroll_into_view_if_needed()
        # self.footer.wait_for(state="attached")


        # last_paragraph = self.scroll_locators.nth(-1)
        # future_paragraph = self.scroll_locators.nth(self.count_paragraph())
        # last_paragraph.wait_for_attached_state()
        # self.footer.scroll_into_view_if_needed()
        # future_paragraph.wait_for_attached_state()

        count_paragraph = self.count_paragraph()
        last_paragraph = self.scroll_locators.nth(-1)
        # future_paragraph = self.scroll_locators.nth(count_paragraph)

        # print(self.count_paragraph(),count_paragraph)
        # if self.count_paragraph() != count_paragraph:
        #     print("зашёл")
        # else:
        #     print("не зашёл")
        last_paragraph.wait_for_attached_state()





        print(f"Количество абзацев {self.count_paragraph()}")

        # next_paragraph.locator.wait_for(state="visible", timeout=3000)
        print(f"scroll_down завершился {self.a} раз")

    def count_paragraph(self):
        return self.scroll_locators.count()
