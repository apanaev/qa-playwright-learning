from playwright.sync_api import Page, Dialog
import logging

logger = logging.getLogger("tests")


class PageActions:
    def __init__(self, page: Page):
        self.page = page

    def goto_url(self, url):
        logger.info(f"Открываю страницу: {url}")
        self.page.goto(url)

    def run_and_accept_alert(self, action):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f"Получаю Alert с текстом: {message}")
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        logger.info("Ожидаю появления Alert")
        action()

        return message

    def run_and_accept_prompt(self, action, random_text):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f"Получаю Prompt с текстом: {message}")
            logger.info(f"Ввожу в Prompt текст: {random_text}")
            dialog.accept(prompt_text=random_text)

        self.page.once("dialog", handle_dialog)
        logger.info("Ожидаю появления Prompt")
        action()
        return message


