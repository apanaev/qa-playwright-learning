import pytest
from playwright.sync_api import Page
from pages.slider_page import SliderPage

from config_reader import ConfigReader
import random

def test_slider(page:Page):

    config = ConfigReader()
    slider_page=SliderPage(page)
    slider_page.goto_url(config.slider_url)

    slider_page.click_and_slide(random.randint(1,9))