
from playwright.sync_api import Page
from ui.page_actions import PageActions


class Slider(PageActions):
    def __init__(self,page: Page):
        super().__init__(page)
