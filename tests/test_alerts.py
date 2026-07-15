from faker import Faker
import pytest
from playwright.sync_api import Page, Locator, Dialog
from pages.alerts_page import AlertPage
from config_reader import ConfigReader

def test_alerts(page: Page):
    fake = Faker("ru_RU")
    random_text = fake.password()

    config = ConfigReader()
    page.goto(config.alert_url)
    page_alerts = AlertPage(page)

    dialog_message = page_alerts.run_and_accept_alert(page_alerts.click_alert_button)
    assert dialog_message == "I am a JS Alert"
    assert page_alerts.get_result_text() == "You successfully clicked an alert"

    dialog_message=page_alerts.run_and_accept_alert(page_alerts.click_confirm_button)
    assert  dialog_message=="I am a JS Confirm"
    assert page_alerts.get_result_text() == "You clicked: Ok"

    dialog_message=page_alerts.run_and_accept_prompt(page_alerts.click_prompt_button, random_text)
    assert dialog_message == "I am a JS prompt"
    assert page_alerts.get_result_text() == "You entered: " + random_text
