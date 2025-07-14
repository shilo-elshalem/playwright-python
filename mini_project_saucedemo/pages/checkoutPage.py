from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # locators:
    TITLE_TEXT = ".title"
    FINISH_BTN = "#finish"
    CANCEL_BTN = "#cancel"
    TOTAL_PRICE_TEXT = "[data-test='total-label']"
    TAX_PRICE_TEXT = "[data-test='tax-label']"
    SUBTOTAL_PRICE_TEXT = "[data-test='subtotal-label']"
    SHIP_INFO_TEXT = "[data-test='shipping-info-value']"
    PAYMENT_INFO_TEXT = "[data-test='payment-info-value']"
    ITEM_QUANTITY_TEXT = ".cart_quantity"
    ITEM_PRICE_TEXT = ".inventory_item_price"
    ITEM_DESC_TEXT = ".inventory_item_desc"
    ITEM_NAME_TEXT = ".inventory_item_name"
    ITEM_AREA = ".cart_item"

    def get_title_page(self):
        return self.get_text(self.TITLE_TEXT)

    def finish(self):
        self.click(self.FINISH_BTN)

    def cancel(self):
        self.click(self.CANCEL_BTN)

    def get_price(self , name_item):
        list_item = self.make_list(self.ITEM_AREA)
        count = list_item.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA,i,self.ITEM_NAME_TEXT) == name_item:
                return self.get_text_in_list(self.ITEM_AREA,i,self.ITEM_PRICE_TEXT)

    def get_desc(self, name_item):
        list_item = self.make_list(self.ITEM_AREA)
        count = list_item.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                return self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_DESC_TEXT)

    def get_quantity(self, name_item):
        list_item = self.make_list(self.ITEM_AREA)
        count = list_item.count()
        for i in range(count):
            if self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_NAME_TEXT) == name_item:
                return self.get_text_in_list(self.ITEM_AREA, i, self.ITEM_QUANTITY_TEXT)

    def make_title_list(self):
        list_item = self.make_list(self.ITEM_AREA)
        count = list_item.count()
        title_list = []
        for i in range(count):
            title_list.append(self.get_text_in_list(self.ITEM_AREA,i, self.ITEM_NAME_TEXT))
        return title_list






