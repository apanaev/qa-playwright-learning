from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.frames_page import FramesPage


def test_frames(page: Page):
    config = ConfigReader()
    frames_page = FramesPage(page)
    frames_page.goto_url(config.frames_url)

    assert frames_page.get_text_left_frame() == "LEFT"
    assert frames_page.get_text_middle_frame() == "MIDDLE"
    assert frames_page.get_text_right_frame() == "RIGHT"
    assert frames_page.get_text_bottom_frame() == "BOTTOM"
