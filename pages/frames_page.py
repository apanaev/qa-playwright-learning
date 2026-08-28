from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class FramesPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.left_frame_locator = WebElement(
            page.frame_locator("//frame[@name='frame-top']").frame_locator("//frame[@name='frame-left']").locator(
                "//body"), "Left frame locator")
        self.middle_frame_locator = WebElement(
            page.frame_locator("//frame[@name='frame-top']").frame_locator("//frame[@name='frame-middle']").locator(
                "//div[@id='content']"), "Middle frame locator")

        self.right_frame_locator = WebElement(
            page.frame_locator("//frame[@name='frame-top']").frame_locator("//frame[@name='frame-right']").locator(
                "//body"), "Right frame locator")
        self.bottom_frame_locator = WebElement(page.frame_locator("//frame[@name='frame-bottom']").locator("//body"),
                                               "Bottom frame locator")

    def get_text_left_frame(self):
        return self.left_frame_locator.get_inner_text()

    def get_text_middle_frame(self):
        return self.middle_frame_locator.get_inner_text()

    def get_text_right_frame(self):
        return self.right_frame_locator.get_inner_text()

    def get_text_bottom_frame(self):
        return self.bottom_frame_locator.get_inner_text()