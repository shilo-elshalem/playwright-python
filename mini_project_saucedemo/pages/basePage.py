import time
from typing import List

from playwright.sync_api import sync_playwright, Page


class BasePage:
    def __init__(self, page:Page):
        self.__page = page

    @property
    def page(self):
        return self.__page

    def fill_text(self, locator, text):
        self.__page.locator(locator).highlight()
        self.__page.locator(locator).fill(text)

    def click(self, locator):
        self.__page.locator(locator).highlight()
        self.__page.locator(locator).click()

    def get_text(self,locator):
        self.__page.locator(locator).highlight()
        text = self.__page.locator(locator).inner_text()
        return text

    #for select:

    def select_option(self, locator, text):
        self.__page.locator(locator).select_option(value=text)

    def select_option_by_text(self, locator, text):
        self.__page.locator(locator).select_option(text)

    def get_chose_value_in_select(self , locator):
        return self.__page.locator(locator).input_value()

    def get_chose_text_in_select(self, locator):
        return self.__page.locator(locator).locator('option:checked').inner_text()


    #for list:

    def make_list (self ,locator):
        list_locators = self.__page.locator(locator)
        return list_locators

    def get_text_in_list(self,locator_area ,i, locator):
        self.__page.locator(locator_area).nth(i).locator(locator).highlight()
        text = self.__page.locator(locator_area).nth(i).locator(locator).inner_text()
        return text

    def click_locator_in_list(self ,locator_area , i ,locator):
        self.__page.locator(locator_area).nth(i).locator(locator).highlight()
        self.__page.locator(locator_area).nth(i).locator(locator).click()

    def fill_text_in_list(self,locator_area , i ,locator , text):
        self.__page.locator(locator_area).nth(i).locator(locator).highlight()
        self.__page.locator(locator_area).nth(i).locator(locator).fill(text)


    #for new tab
    def get_url_new_tab(self):
        return self.page.context.pages[-1].url

    def close_new_tab(self):
        self.page.context.pages[-1].close()

    def click_and_return_new_page(self,locator):
        self.__page.locator(locator).click()
        self.__page.context.pages[-1].wait_for_load_state()
        return self.__page.context.pages[-1]

    #def wait_for_load_new_page(self):
    #    self.__page.context.pages[-1].wait_for_load_state()
#
    #def return_new_page_url(self):
    #    self.__page.context.pages[-1].wait_for_load_state()
    #    return self.__page.context.pages[-1].url