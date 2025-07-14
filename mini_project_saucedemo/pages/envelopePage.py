from time import sleep

from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class EnvelopePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # locators:
    MENU_BTN = "#react-burger-menu-btn"
    MENU_PRODUCTS_BTN = "#inventory_sidebar_link"
    MENU_ABOUT_BTN = "#about_sidebar_link"
    MENU_LOGOUT_BTN = "#logout_sidebar_link"
    MENU_RESET_BTN = "#reset_sidebar_link"
    CLOSE_MENU_BTN = "#react-burger-cross-btn"
    TWITTER_BTN =".social_twitter"
    FACEBOOK_BTN =".social_facebook"
    LINKEDIN_BTN =".social_linkedin"

    def open_menu(self):
        self.click(self.MENU_BTN)

    def chose_all_items(self):
        self.click(self.MENU_PRODUCTS_BTN)

    def chose_about(self):
        self.click(self.MENU_ABOUT_BTN)

    def chose_logout(self):
        self.click(self.MENU_LOGOUT_BTN)

    def chose_reset(self):
        self.click(self.MENU_RESET_BTN)

    def open_menu_and_chose_all_items(self):
        self.click(self.MENU_BTN)
        self.click(self.MENU_PRODUCTS_BTN)

    def open_menu_and_chose_about(self):
        self.click(self.MENU_BTN)
        self.click(self.MENU_ABOUT_BTN)

    def open_menu_and_chose_logout(self):
        self.click(self.MENU_BTN)
        self.click(self.MENU_LOGOUT_BTN)

    def open_menu_and_chose_reset(self):
        self.click(self.MENU_BTN)
        self.click(self.MENU_RESET_BTN)

    def open_twitter(self):
        self.click(self.TWITTER_BTN)
        self.page.context.pages[-1].wait_for_timeout(3000)

    def open_facebook(self):
        self.click(self.FACEBOOK_BTN)
        self.page.context.pages[-1].wait_for_timeout(3000)

    def open_linkedin(self):
        self.click(self.LINKEDIN_BTN)
        self.page.context.pages[-1].wait_for_timeout(3000)
