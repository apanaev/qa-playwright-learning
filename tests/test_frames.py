from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.frames_page import FramesPage


def test_frames(page: Page):
    config = ConfigReader()
    frames_page = FramesPage(page)
    frames_page.goto_url(config.frames_url)

    text_left_frame = frames_page.get_text_left_frame()
    text_middle_frame = frames_page.get_text_middle_frame()
    text_right_frame = frames_page.get_text_right_frame()
    text_bottom_frame = frames_page.get_text_bottom_frame()

    assert text_left_frame == "LEFT", f"Ожидали: 'LEFT', а получили: {text_left_frame}"
    assert text_middle_frame == "MIDDLE", f"Ожидали: 'MIDDLE', а получили: {text_middle_frame}"
    assert text_right_frame == "RIGHT", f"Ожидали: 'RIGHT', а получили: {text_right_frame}"
    assert text_bottom_frame == "BOTTOM", f"Ожидали: 'BOTTOM', а получили: {text_bottom_frame}"
