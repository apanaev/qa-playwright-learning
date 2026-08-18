from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.dynamic_content_page import DynamicContentPage


def tests_dynamic_content(page:Page):
    config = ConfigReader()
    dynamic_content_page = DynamicContentPage(page)
    dynamic_content_page.goto_url(config.dynamic_contest_url)


    while dynamic_content_page.get_unique_images_count() == 3:
        dynamic_content_page.reload_page()

    assert dynamic_content_page.get_unique_images_count() !=3
