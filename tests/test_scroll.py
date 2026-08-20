from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.scroll_page import ScrollPage
from playwright.sync_api import expect


def test_scroll(page: Page):
    config = ConfigReader()
    scroll_page = ScrollPage(page)
    scroll_page.goto_url(config.scroll_url)

    count = scroll_page.scroll_locators.count()
    while count < 10:
        scroll_page.scroll_down()
        # expect(scroll_page.scroll_locators.locator).not_to_have_count(count) Не рабочий метод оставил, чтоб показать что я пытался дождаться загрузки, и только потом считать абзацы
        count = scroll_page.scroll_locators.count()
    assert count >=10

