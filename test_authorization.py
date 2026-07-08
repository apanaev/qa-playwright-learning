import pytest
from playwright.sync_api import Page

from config_reader import ConfigReader


def test_authorization(browser):
    config = ConfigReader()
    context = browser.new_context(http_credentials={"username": config.login, "password": config.password})
    page = context.new_page()
    page.goto(config.main_url)
