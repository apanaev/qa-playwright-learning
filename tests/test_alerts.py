from faker import Faker
import pytest
from playwright.sync_api import Page, Locator,Dialog
from pages.alerts_page import AlertPage
from config_reader import ConfigReader




def test_alerts(page: Page):
    fake = Faker("ru_RU")
    random_text = fake.password()

    def alert_dialog(dialog: Dialog):
        assert dialog.message == "I am a JS Alert"
        dialog.accept()

    def confirm_dialog(dialog: Dialog):
        assert dialog.message == "I am a JS Confirm"
        dialog.accept()

    def prompt_dialog(dialog: Dialog):
        assert dialog.message == "I am a JS prompt"
        dialog.accept(prompt_text=random_text)

    config = ConfigReader()
    page.goto(config.alert_url)
    page_alerts = AlertPage(page)

    page.on("dialog", alert_dialog)
    page_alerts.click_alert_button()
    assert page_alerts.get_result_text() == "You successfully clicked an alert"
    page.remove_listener("dialog", alert_dialog)

    page.on("dialog", confirm_dialog)
    page_alerts.click_confirm_button()
    assert page_alerts.get_result_text() == "You clicked: Ok"
    page.remove_listener("dialog", confirm_dialog)

    page.on("dialog", prompt_dialog)
    page_alerts.click_prompt_button()
    assert page_alerts.get_result_text() == "You entered: " + random_text
    page.remove_listener("dialog", prompt_dialog)
