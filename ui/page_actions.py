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

    def expect_new_page(self, action):
        logger.info("Ожидаю появления новой страницы для выполнения действия")
        with self.page.expect_popup() as popup_info:
            action()
        return popup_info.value

    def bring_to_front(self, target_page: Page):
        logger.info(f"Переключаюсь на вкладку: {target_page.url}")
        target_page.bring_to_front()

    def close_page(self, target_page: Page):
        logger.info(f"Закрываю вкладку: {target_page.url}")
        target_page.close()
