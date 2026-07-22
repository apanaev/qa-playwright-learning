import pytest
from playwright.sync_api import Page
from pages.slider_page import Slider

from config_reader import ConfigReader

def test_slider(page:Page):

    config = ConfigReader()
    slider_page=Slider(page)
    slider_page.goto_url(config.slider_url)