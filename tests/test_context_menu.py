import pytest
from playwright.sync_api import Page, Locator, Dialog
from pages.context_menu_page import ContextMenuPage
from config_reader import ConfigReader


def test_context_menu(page: Page):
    config = ConfigReader()
    context_menu_page = ContextMenuPage(page)
    context_menu_page.goto_url(config.context_menu_url)
    message = context_menu_page.run_and_accept_alert(context_menu_page.right_click_context_menu)

    assert message == "You selected a context menu"
