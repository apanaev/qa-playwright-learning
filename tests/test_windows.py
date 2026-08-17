from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.windows_page import WindowsPage
from ui.web_element import WebElement


def test_windows(page: Page):
    config = ConfigReader()
    windows_page = WindowsPage(page)
    windows_page.goto_url(config.windows_url)

    new_page, new_page_text = windows_page.open_new_window_and_get_text()
    assert new_page_text == "New Window"

    windows_page.bring_to_front(page)

    new_page2, new_page2_text = windows_page.open_new_window_and_get_text()
    assert new_page2_text == "New Window"

    windows_page.bring_to_front(page)

    windows_page.close_page(new_page)

    windows_page.close_page(new_page2)

    assert len(page.context.pages) == 1
