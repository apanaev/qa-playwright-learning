from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page

class DynamicContentPage(PageActions):
    def __init__(self,page : Page):
        super().__init__(page)
        self.first_image = MultiWebElement( page.locator("//div[@class='large-2 columns']"),"Изображения" )       # "page.get_attribute("src")"

