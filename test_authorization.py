import pytest
from playwright.sync_api import Page


def test_authorization(page: Page):
    print(page)