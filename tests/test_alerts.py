from faker import Faker
import pytest
from playwright.sync_api import Page, Locator, Dialog

import logging
from pages.alerts_page import AlertPage
from config_reader import ConfigReader

logger = logging.getLogger("tests")


def test_alerts(page: Page):
    fake = Faker("ru_RU")
    random_text = fake.password()

    config = ConfigReader()
    # page.goto(config.alert_url)
    page_alerts = AlertPage(page)
    page_alerts.goto_url(config.alert_url)

    logger.info("========== ALERT ==========")
    dialog_message = page_alerts.run_and_accept_alert(page_alerts.click_alert_button)
    assert dialog_message == "I am a JS Alert"
    assert page_alerts.get_result_text() == "You successfully clicked an alert"
    logger.info("")

    logger.info("========== CONFIRM ==========")
    dialog_message = page_alerts.run_and_accept_alert(page_alerts.click_confirm_button)
    assert dialog_message == "I am a JS Confirm"
    assert page_alerts.get_result_text() == "You clicked: Ok"
    logger.info("")

    logger.info("========== PROMPT ==========")
    dialog_message = page_alerts.run_and_accept_prompt(page_alerts.click_prompt_button, random_text)
    assert dialog_message == "I am a JS prompt"
    assert page_alerts.get_result_text() == "You entered: " + random_text
    logger.info("")
