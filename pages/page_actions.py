from playwright.sync_api import Page, Dialog
import logging

logger = logging.getLogger("tests")


class PageActions:
    def __init__(self, page: Page):
        self.page = page
        logger.info("PageActions initialized")

    def goto_url(self, url):
        logger.info(f"Navigated to: {url}")
        self.page.goto(url)


    def run_and_accept_alert(self, action):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f"Dialog message: {message}")
            dialog.accept()
            logger.info("Dialog accepted ")

        self.page.once("dialog", handle_dialog)
        logger.info("Launching action")
        action()

        return message

    def run_and_accept_prompt(self, action, random_text):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f"Dialog  message: {message}")
            dialog.accept(prompt_text=random_text)
            logger.info(f"Dialog  accepted with text: {random_text}")

        self.page.once("dialog", handle_dialog)
        logger.info("Launching action")
        action()
        return message
