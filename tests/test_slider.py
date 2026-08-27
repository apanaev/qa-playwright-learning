from playwright.sync_api import Page
from pages.slider_page import SliderPage

from config_reader import ConfigReader
import random


def test_slider(page: Page):
    config = ConfigReader()
    slider_page = SliderPage(page)
    slider_page.goto_url(config.slider_url)

    random_press_right = random.randint(1, 9)

    slider_page.focus_and_slide(random_press_right)
    value_slide = float(slider_page.get_slider_value())
    step = 0.5

    assert value_slide == step * random_press_right
