import logging

from faker import Faker
from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.alerts_page import AlertPage

logger = logging.getLogger("tests")


def test_alerts(page: Page):
    fake = Faker("ru_RU")
    random_text = fake.password()

    config = ConfigReader()
    page_alerts = AlertPage(page)
    page_alerts.goto_url(config.alert_url)

    logger.info("========== ALERT ==========")
    dialog_message = page_alerts.run_and_accept_alert(page_alerts.click_alert_button)
    assert dialog_message == "I am a JS Alert", f"Ожидали: 'I am a JS Alert', а получили:  {dialog_message}"
    result = page_alerts.get_result_text()
    assert result == "You successfully clicked an alert", f"Ожидали: 'You successfully clicked an alert', а получили: {result}"
    logger.info("")

    logger.info("========== CONFIRM ==========")
    dialog_message = page_alerts.run_and_accept_alert(page_alerts.click_confirm_button)
    assert dialog_message == "I am a JS Confirm", f"Ожидали: 'I am a JS Confirm', а получили:  {dialog_message}"
    result = page_alerts.get_result_text()
    assert result == "You clicked: Ok", f"Ожидали: 'You clicked: Ok', а получили {result}"
    logger.info("")

    logger.info("========== PROMPT ==========")
    dialog_message = page_alerts.run_and_accept_prompt(page_alerts.click_prompt_button, random_text)
    assert dialog_message == "I am a JS prompt", f"Ожидали: 'I am a JS prompt', а получили:  {dialog_message}"
    result = page_alerts.get_result_text()
    assert result == "You entered: " + random_text, f"Ожидали: You entered: {random_text}, а получили {result}"
    logger.info("")
