import logging

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement

logger = logging.getLogger("tests")


class SliderPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.slider_locator = WebElement(
            page.locator("//div[contains(@class, 'slider') and contains(@class, 'Container')]//input[@type='range']"),
            "Слайдер")
        self.slider_value = WebElement(page.locator("//*[@id='range']"), "Значение слайдера")

    def focus_and_slide(self, press_count):
        self.slider_locator.focus()
        for i in range(0, press_count):
            self.slider_locator.press_button('ArrowRight')

    def get_slider_value(self):
        return self.slider_value.get_inner_text()

    def get_slider_step(self):
        return float(self.slider_locator.get_attribute("step"))

    def get_min_value_slider(self):
        return float(self.slider_locator.get_attribute("min"))

    def get_max_value_slider(self):
        return float(self.slider_locator.get_attribute("max"))
