from playwright.sync_api import Locator
import logging

logger = logging.getLogger("tests")


class WebElement:
    def __init__(self, locator: Locator, description):
        self.locator = locator
        self.description = description

    def get_inner_text(self):
        text=self.locator.inner_text()
        logger.info(f"Получаю текст элемента: {self.description}")
        logger.info(f"Получил текст: {text}")
        return text

    def click(self):
        logger.info(f"Кликаю на элемент: {self.description}")
        self.locator.click()

