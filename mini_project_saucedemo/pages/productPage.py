from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locatiors:
    BAKE_TO_PRODUCTS_BTN = "#back-to-products"
    PRICE_TEXT = ".inventory_details_price"
    DESC_TEXT = ".inventory_details_desc"
    NAME_PRODUCT_TEXT = ".inventory_details_name"
    ADD_TO_CART_BTN = "#add-to-cart"
    REMOVE_BTN = "#remove"
    BTN_REMOVE_OR_ADD_BTN = ".btn_inventory"
    CART_BTN = ".shopping_cart_link"

    def bake_to_products(self):
        self.click(self.BAKE_TO_PRODUCTS_BTN)

    def get_price_text(self):
        price_text = self.get_text(self.PRICE_TEXT)
        return price_text

    def get_price_num(self):
        price_text = self.get_text(self.PRICE_TEXT)
        price_num = price_text.replace("$","")
        return price_num

    def get_desc(self):
        desc = self.get_text(self.DESC_TEXT)
        return desc

    def get_name_product(self):
        name = self.get_text(self.NAME_PRODUCT_TEXT)
        return name

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def remove(self):
        self.click(self.REMOVE_BTN)

    def click_btn_add_or_remove(self):
        self.click(self.BTN_REMOVE_OR_ADD_BTN)

    def get_text_in_btn(self):
        text = self.get_text(self.BTN_REMOVE_OR_ADD_BTN)
        return text

    def open_cart(self):
        self.click(self.CART_BTN)