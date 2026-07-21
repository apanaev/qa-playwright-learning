from playwright.sync_api import Page, Locator
from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertPage(PageActions):

    def __init__(self, page: Page):
        super().__init__(page)
        # self.alert_button: Locator = page.locator("//*[@onclick='jsAlert()']")
        self.alert_button = WebElement(page.locator("//*[@onclick='jsAlert()']"), "Кнопка JS Alert")
        self.confirm_button = WebElement(page.locator("//*[@onclick='jsConfirm()']"),"Кнопка JS Confirm")
        self.prompt_button = WebElement(page.locator("//*[@onclick='jsPrompt()']"),"Кнопка JS Prompt")
        self.result_locator = WebElement(page.locator("//*[@id='result']"),"Поле результата")

    def click_alert_button(self):
        self.alert_button.click()

    def get_result_text(self):
        return self.result_locator.get_inner_text()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_prompt_button(self):
        self.prompt_button.click()
