import tempfile
from pathlib import Path

from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.file_upload_page import FileUpload


def test_file_upload(page: Page):
    config = ConfigReader()
    file_upload_page = FileUpload(page)
    file_upload_page.goto_url(config.file_upload_url)

    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp_file:
        tmp_file.write(b"some content")
        path = tmp_file.name

    result_text = file_upload_page.set_input_file(path)

    filename = Path(path).name
    assert result_text == filename
