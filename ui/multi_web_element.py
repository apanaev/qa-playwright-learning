from playwright.sync_api import Locator
import logging

from ui.web_element import WebElement

logger = logging.getLogger("tests")


class MultiWebElement:
    def __init__(self, locator: Locator, description):
        self.locator = locator
        self.description = description


    def count(self):
        count_element =self.locator.count()
        logger.info(f"Найдено {count_element} элементов: {self.description} ")
        return count_element

    def nth(self,index):
        locator = self.locator.nth(index)
        locator = WebElement
        return locator

