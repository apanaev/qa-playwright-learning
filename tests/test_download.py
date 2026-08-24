from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.download_page import DownloadPage


def test_download(page:Page):
    config = ConfigReader ()
    download_page = DownloadPage (page)

    download_page.goto_url(config.download_url)


