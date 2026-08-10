from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.windows_page import WindowsPage
from ui.web_element import WebElement


def test_windows(page: Page):
    config = ConfigReader()
    windows_page = WindowsPage(page)
    windows_page.goto_url(config.windows_url)

    new_page = windows_page.expect_new_page(windows_page.windows_locator.click)
    new_page_text = WebElement(new_page.locator("//h3"), "Текст нового окна")
    assert new_page_text.get_inner_text() == "New Window"

    windows_page.bring_to_front(page)

    new_page2 = windows_page.expect_new_page(windows_page.windows_locator.click)
    new_page2_text = WebElement(new_page2.locator("//h3"), "Текст нового окна")
    assert new_page2_text.get_inner_text() == "New Window"

    windows_page.bring_to_front(page)

    windows_page.close_page(new_page)

    windows_page.close_page(new_page2)

    assert len(page.context.pages) == 1
