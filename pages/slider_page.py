from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class SliderPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.slider_locator = WebElement(page.locator("//div[@class='sliderContainer']//input[@type='range']"),
                                         "Слайдер")
        self.slider_value = WebElement(page.locator("//*[@id='range']"), "Значение слайдера")

    def click_and_slide(self,press_count):
        self.slider_locator.click()
        for i in range(0,press_count):
            self.slider_locator.press_button('ArrowRight')




