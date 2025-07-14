from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class LoginPage (BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    #locators:
    __USER_NAME_FIELD = "#user-name"
    __PASSWORD_FIELD = "#password"
    __LOGIN_BTN = "#login-button"
    __ERROR_TEXT = ".error-message-container"
    __ERROR_X_BTN = ".error button"

    def fill_details_and_login(self,user_name,password):
        self.fill_text(self.__USER_NAME_FIELD,user_name)
        self.fill_text(self.__PASSWORD_FIELD,password)
        self.click(self.__LOGIN_BTN)

    def fill_details_without_login(self,user_name,password):
        self.fill_text(self.__USER_NAME_FIELD,user_name)
        self.fill_text(self.__PASSWORD_FIELD,password)

    def fill_user_name(self,user_name):
        self.fill_text(self.__USER_NAME_FIELD,user_name)

    def fill_password(self,password):
        self.fill_text(self.__PASSWORD_FIELD,password)

    def click_btn_login(self):
        self.click(self.__LOGIN_BTN)

    def get_error(self):
        return self.get_text(self.__ERROR_TEXT)

    def close_error(self):
        self.click(self.__ERROR_X_BTN)




