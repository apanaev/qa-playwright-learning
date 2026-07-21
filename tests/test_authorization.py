import pytest
from playwright.sync_api import Page, Locator
from pages.authorization_page import AuthorizationPage

from config_reader import ConfigReader


def test_authorization(browser):
    config = ConfigReader()
    context = browser.new_context(http_credentials={"username": config.login, "password": config.password})
    page = context.new_page()
    authorization_page = AuthorizationPage(page)
    authorization_page.goto_url(config.main_url)

    assert authorization_page.get_success_message() == "Congratulations! You must have the proper credentials."
