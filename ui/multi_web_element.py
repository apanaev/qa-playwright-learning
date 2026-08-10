from playwright.sync_api import Locator
import logging

from ui.web_element import WebElement

logger = logging.getLogger("tests")


class MultiWebElement:
    def __init__(self, locator: Locator, description):
        self.locator = locator
        self.description = description

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= self.count():
            raise StopIteration
        else:
            element = self.nth(self._index)
            self._index += 1
            return element

    def count(self):
        count_element = self.locator.count()
        return count_element

    def nth(self, index):
        locator = self.locator.nth(index)
        element = WebElement(locator, f"{self.description}[{index}]")
        return element
