import pytest
from playwright.sync_api import Page, Locator, Dialog
from pages.context_menu_page import ContextMenuPage
from config_reader import ConfigReader


def test_context_menu(page: Page):

    def context_dialog(dialog: Dialog):
        assert dialog.message == "You selected a context menu"
        dialog.accept()

    config = ConfigReader()
    page.goto(config.context_menu_url)
    context_menu_page = ContextMenuPage(page)

    page.on("dialog", context_dialog)
    context_menu_page.right_click_context_menu()
    page.remove_listener("dialog", context_dialog)

