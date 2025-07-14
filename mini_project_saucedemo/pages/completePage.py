from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class CompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # locators:
    TITLE_TEXT = ".title"
    BAKE_HOME_BTN = "#back-to-products"
    MESSAGE_TEXT = ".complete-text"
    HEADER_TEXT = ".complete-header"

    def get_title_page(self):
        return self.get_text(self.TITLE_TEXT)

    def click_bake_home(self):
        self.click(self.BAKE_HOME_BTN)

    def get_message(self):
        self.get_text(self.MESSAGE_TEXT)

    def get_header(self):
        self.get_text(self.HEADER_TEXT)
