from playwright.sync_api import Page, Dialog
import logging


logger = logging.getLogger(__name__)

class PageActions:
    def __init__(self, page: Page):
        self.page = page
        logger.info("PageActions initialized")

    def run_and_accept_alert(self, action):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            logger.info(f"Alert text: {message}")
            dialog.accept()
            logger.info(f"Alert accepted {message}")

        self.page.once("dialog", handle_dialog)
        logger.info(f"Launching action")
        action()

        return message

    def run_and_accept_prompt(self, action, random_text):
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message
            dialog.accept(prompt_text=random_text)

        self.page.once("dialog", handle_dialog)
        action()
        return message