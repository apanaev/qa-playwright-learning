from playwright.sync_api import Locator
import logging

logger = logging.getLogger("tests")


class WebElement:
    def __init__(self, locator: Locator, description):
        self.locator = locator
        self.description = description

    def get_inner_text(self):
        logger.info(f"Получаю текст элемента: {self.description}")
        text = self.locator.inner_text()
        logger.info(f"Получил текст: {text}")
        return text

    def click(self):
        logger.info(f"Кликаю на элемент: {self.description}")
        self.locator.click()

    def right_click(self):
        logger.info(f"Кликаю правой кнопкой мыши на элемент: {self.description}")
        self.locator.click(button="right")

    def press_button(self, button):
        logger.info(f"На элементе: {self.description} нажимаю клавишу {button}")
        self.locator.press(key=button)

    def focus(self):
        logger.info(f"Устанавливаю фокус на: {self.description}")
        self.locator.focus()

    def hover(self):
        logger.info(f"Навожусь мышкой на: {self.description}")
        self.locator.first.hover()

    def scroll_into_view_if_needed(self) :
        logger.info(f": Прокручиваю к элементу { self.description}, если он не виден")
        self.locator.scroll_into_view_if_needed()
