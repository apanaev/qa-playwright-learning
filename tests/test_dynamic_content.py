from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.dynamic_content_page import DynamicContentPage


def tests_dynamic_content(page:Page):
    config = ConfigReader()
    dynamic_content_page = DynamicContentPage(page)
    dynamic_content_page.goto_url(config.dynamic_contest_url)

    dynamic_content_page.reload_page()
    print(dynamic_content_page.first_image.count())

    first = dynamic_content_page.first_image.nth(0)
    img_locator=first.locator.locator("//img")
    src=img_locator.get_attribute("src")
    print(src)