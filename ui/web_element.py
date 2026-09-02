import logging

from playwright.sync_api import Locator

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

    def scroll_into_view_if_needed(self):
        logger.info(f"Прокручиваю к элементу {self.description}, если он не виден")
        self.locator.scroll_into_view_if_needed()

    def set_input_file(self, path_file):
        logger.info(f"Загружаю файл находящийся по пути {path_file}")
        self.locator.set_input_files(path_file)

    def get_attribute(self, attribute):
        logger.info(f"Получаю атрибут {attribute} с элемента {self.description}")
        return self.locator.get_attribute(attribute)

    def wait_for_attached_state(self):
        logger.info(f"Ожидаю загрузки {self.description}")
        self.locator.wait_for(state="attached")
