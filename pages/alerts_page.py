from playwright.sync_api import Page, Locator,Dialog
from pages.page_actions import PageActions


class AlertPage(PageActions):

    def __init__(self, page: Page):
        super().__init__(page)
        self.alert_button: Locator = page.locator("//*[@onclick='jsAlert()']")
        self.confirm_button: Locator = page.locator("//*[@onclick='jsConfirm()']")
        self.prompt_button: Locator = page.locator("//*[@onclick='jsPrompt()']")
        self.result_locator: Locator = page.locator("//*[@id='result']")

    def click_alert_button(self):
        self.alert_button.click()

    def get_result_text(self):
        return self.result_locator.inner_text()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_prompt_button(self):
        self.prompt_button.click()




