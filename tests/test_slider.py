import random

from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.slider_page import SliderPage


def test_slider(page: Page):
    config = ConfigReader()
    slider_page = SliderPage(page)
    slider_page.goto_url(config.slider_url)

    step = slider_page.get_slider_step()
    min_value_slider = slider_page.get_min_value_slider()
    max_value_slider = slider_page.get_max_value_slider()


    total_step_slider = (max_value_slider - min_value_slider) / step
    random_press_right = random.randint(1, int(total_step_slider) - 1)

    slider_page.focus_and_slide(random_press_right)
    value_slide = float(slider_page.get_slider_value())

    expected_value = min_value_slider + step * random_press_right
    assert value_slide == expected_value, f"Ожидали: {expected_value}, а получили: {value_slide}"
