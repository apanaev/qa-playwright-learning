from playwright.sync_api import Page
from config_reader import ConfigReader
from pages.scroll_page import ScrollPage


def test_scroll(page: Page):  # тест не рабочий без таймаута не получается победить,
    config = ConfigReader()
    scroll_page = ScrollPage(page)
    scroll_page.goto_url(config.scroll_url)


    count = scroll_page.scroll_locators.count()
    while count < 10:
        scroll_page.scroll_down()
        count = scroll_page.scroll_locators.count()