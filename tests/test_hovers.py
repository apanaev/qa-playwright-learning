from playwright.sync_api import Page
from config_reader import ConfigReader
from pages.hovers_page import HoversPage


def test_hovers(page:Page):
    config = ConfigReader()
    hovers_page = HoversPage(page)
    hovers_page.goto_url(config.hovers_url)

    hovers_page.foo()
    name_user = hovers_page.get_user()


    assert name_user == "name: user1"




