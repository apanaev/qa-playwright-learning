from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.windows_page import WindowsPage


def test_windows(page: Page):
    config = ConfigReader()
    windows_page = WindowsPage(page)
    windows_page.goto_url(config.windows_url)

    new_page = windows_page.open_new_window()
    new_page_text = new_page.get_text()
    assert new_page_text == "New Window"

    windows_page.bring_to_front(page)

    new_page2 = windows_page.open_new_window()
    new_page2_text = new_page2.get_text()

    assert new_page2_text == "New Window"

    windows_page.bring_to_front(page)

    new_page.close_page()

    new_page2.close_page()

    assert len(page.context.pages) == 1
