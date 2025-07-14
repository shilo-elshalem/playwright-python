from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class InformationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # locators:
    TITLE_TEXT = ".title"
    FIRST_NAME_FIELD = "#first-name"
    LAST_NAME_FIELD = "#last-name"
    POSTAL_CODE_FIELD = "#postal-code"
    CANSEL_BTN = "#cancel"
    CONTINUE_BTN = "#continue"
    ERROR_TEXT = ".error-message-container h3"

    def get_title_page(self):
        return self.get_text(self.TITLE_TEXT)

    def fill_information_and_continue(self,first_name,last_name,postal_code):
        self.fill_text(self.FIRST_NAME_FIELD,first_name)
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        self.fill_text(self.POSTAL_CODE_FIELD, postal_code)
        self.click(self.CONTINUE_BTN)

    def fill_information_without_continue(self, first_name, last_name, postal_code):
        self.fill_text(self.FIRST_NAME_FIELD, first_name)
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        self.fill_text(self.POSTAL_CODE_FIELD, postal_code)

    def fill_first_name(self,first_name):
        self.fill_text(self.FIRST_NAME_FIELD,first_name)

    def fill_last_name(self,last_name):
        self.fill_text(self.LAST_NAME_FIELD,last_name)

    def fill_postal_code(self,postal_code):
        self.fill_text(self.POSTAL_CODE_FIELD,postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def click_cancel(self):
        self.click(self.CANSEL_BTN)

    def get_error_text(self):
        return self.get_text(self.ERROR_TEXT)


