from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.download_page import DownloadPage


def test_download(page: Page):
    config = ConfigReader()
    download_page = DownloadPage(page)

    download_page.goto_url(config.download_url)

    text_third_link,third_link = download_page.get_text_third_link_and_text()
    download_file= download_page.expect_download(third_link.click)
    assert download_file.suggested_filename == text_third_link
