from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.hovers_page import HoversPage


def test_hovers(page: Page):
    config = ConfigReader()
    hovers_page = HoversPage(page)
    hovers_page.goto_url(config.hovers_url)

    for index, avatar in enumerate(hovers_page.avatar_locator):
        avatar.hover()
        user_name = hovers_page.get_user(index)
        expected_name = f"name: user{index + 1}"
        assert user_name == expected_name, f"Ожидали: {expected_name}, а получили: {user_name}"
        index += 1
