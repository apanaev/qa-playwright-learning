import random

from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.slider_page import SliderPage


def test_slider(page: Page):
    config = ConfigReader()
    slider_page = SliderPage(page)
    slider_page.goto_url(config.slider_url)

    step = float(slider_page.slider_locator.get_attribute("step"))
    min_value_slider = float(slider_page.slider_locator.get_attribute("min"))
    max_value_slider = float(slider_page.slider_locator.get_attribute("max"))

    total_step_slider = (max_value_slider - min_value_slider) / step
    random_press_right = random.randint(1, int(total_step_slider) - 1)

    slider_page.focus_and_slide(random_press_right)
    value_slide = float(slider_page.get_slider_value())

    assert value_slide == min_value_slider + step * random_press_right
