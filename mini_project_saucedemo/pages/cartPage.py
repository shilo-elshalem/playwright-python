from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage
from mini_project_saucedemo.pages.envelopePage import EnvelopePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        #self.envelopePage = EnvelopePage

    #locators:
    TITLE_TEXT = ".title"
    ITEM_AREA = ".cart_item"
    QUANTITY_FOR_ITEM_TEXT = ".cart_quantity"
    ITEM_NAME_TEXT =".inventory_item_name"
    ITEM_DESC_TEXT = ".inventory_item_desc"
    ITEM_PRICE_TEXT = ".inventory_item_price"
    REMOVE_ITEM_BTN ="[id ^= 'remove']"
    CHECKOUT_BTN = "#checkout"
    CONTINUE_BTN = "#continue-shopping"
    NUM_IN_CART_TEXT =".shopping_cart_badge"

    def get_title_page(self):
        return self.get_text(self.TITLE_TEXT)

    def make_string_list_of_names_items(self):
        list_items =self.make_list(self.ITEM_AREA)
        count = list_items.count()
        list_names_items = []
        for i in range(count):
            list_names_items.append(self.get_text_in_list(self.ITEM_AREA,i,self.ITEM_NAME_TEXT))
        return list_names_items

    def remove_item(self , name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA,i,self.ITEM_NAME_TEXT)==name_item:
                self.click_locator_in_list(self.ITEM_AREA,i,self.REMOVE_ITEM_BTN)
                break

    def enter_to_item(self,name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                self.click_locator_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT)
                break

    def return_descriptions_item(self,name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                desc_item =self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_DESC_TEXT)
                return desc_item

    def return_item_price_text(self,name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                item_price_text =self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_PRICE_TEXT)
                return item_price_text

    def return_item_price_num(self,name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                item_price_text =self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_PRICE_TEXT)
                item_price_num = float(item_price_text.replace("$",""))
                return item_price_num

    def return_quantity_item(self,name_item):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                quantity_item =self.get_text_in_list(self.ITEM_AREA, i, self.QUANTITY_FOR_ITEM_TEXT)
                return quantity_item

    def return_sum_items(self):
        list_items = self.make_list(self.ITEM_AREA)
        count = list_items.count()
        return count

    def continue_shopping(self):
        self.click(self.CONTINUE_BTN)

    def checkout(self):
        self.click(self.CHECKOUT_BTN)