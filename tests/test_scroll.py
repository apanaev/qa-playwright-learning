from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.scroll_page import ScrollPage


def test_scroll(page: Page):
    config = ConfigReader()
    scroll_page = ScrollPage(page)
    scroll_page.goto_url(config.scroll_url)

    count = scroll_page.count_paragraf()
    while count < 10:
        scroll_page.scroll_down()
        count = scroll_page.count_paragraf()

    print(f"Метод scroll_page.scroll_down() запускается {scroll_page.iterr} раз")

