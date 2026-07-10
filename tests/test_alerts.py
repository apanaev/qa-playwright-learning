from playwright.sync_api import Dialog

import pytest
from playwright.sync_api import Page, Locator
from pages.alerts_page import AlertPage
from config_reader import ConfigReader


def test_alerts(page: Page):
    config = ConfigReader()

    page.goto(config.alert_url)
    page_alerts = AlertPage(page)
    page.on("dialog", handle_dialog)
    page_alerts.click_alert_button()


def handle_dialog(dialog: Dialog):
    assert dialog.message == "I am a JS Alert"
    dialog.accept()
