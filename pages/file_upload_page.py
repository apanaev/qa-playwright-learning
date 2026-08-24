from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class FileUpload(PageActions):
    def __init__(self,page : Page):
        super().__init__(page)
        self.select_file_locator = WebElement(page.locator("//*[@id='file-upload']"),"Выберите файл")
        self.upload_locator = WebElement (page.locator("//*[@id='file-submit']"),"Upload")
        self.result_locator = WebElement (page.locator('//*[@id="uploaded-files"]'),"Название файла")

    def set_input_file(self,path_file):
        self.select_file_locator.set_input_file(path_file)
        self.upload_locator.click()
        return self.result_locator.get_inner_text()
