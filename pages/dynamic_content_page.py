from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page


class DynamicContentPage(PageActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.div_images = MultiWebElement(page.locator("//div[@class='large-2 columns']"),
                                          "Изображения")

    def get_unique_images_count(self):
        unique_div_set = set()
        for image_div in self.div_images:
            img_src = image_div.locator.locator("//img").get_attribute("src")
            unique_div_set.add(img_src)

        return len(unique_div_set)
