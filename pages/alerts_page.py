from playwright.sync_api import Page, Locator


class AlertPage:

    def __init__(self, page: Page):
        self.page = page
        self.alert_button: Locator = page.locator("//*[@onclick='jsAlert()']")

    def click_alert_button(self):
        self.alert_button.click()
