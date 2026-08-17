from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.frames_page import FramesPage


def test_frames(page: Page):
    config = ConfigReader()
    frames_page = FramesPage(page)
    frames_page.goto_url(config.frames_url)

    assert frames_page.left_frame_locator.get_inner_text() == "LEFT"
    assert frames_page.middle_frame_locator.get_inner_text() == "MIDDLE"
    assert frames_page.right_frame_locator.get_inner_text() == "RIGHT"
    assert frames_page.bottom_frame_locator.get_inner_text() == "BOTTOM"
