from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement


class DynamicContentPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.div_images = MultiWebElement(
            page.locator("//div[contains(@class, 'large-2') and contains(@class, 'columns')]"),
            "Изображения")

    def get_unique_images_count(self):
        unique_div_set = set()
        for image_div in self.div_images:
            img_src = WebElement(image_div.locator.locator("//img"), "Изображение")
            img_src = img_src.get_attribute("src")
            unique_div_set.add(img_src)

        return len(unique_div_set)
