from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.file_upload_page import FileUpload
from pathlib import Path


def test_file_upload(page: Page):
    config = ConfigReader()
    file_upload_page = FileUpload(page)
    file_upload_page.goto_url(config.file_upload_url)

    path = Path(r"C:\Users\Руслан\Downloads\Счет на оплату № 822 от 21 августа 2026 г.pdf")

    result_text = file_upload_page.set_input_file(path)
    filename = path.name
    assert result_text == filename
