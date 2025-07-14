from playwright.sync_api import Page

from mini_project_saucedemo.pages.basePage import BasePage

class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    #locators:
    TITLE_TEXT = ".title"
    PRODUCT_AREA = ".inventory_item"
    PRODUCT_TITLE = ".inventory_item_name"
    PRODUCT_DESC_TEXT = ".inventory_item_desc"
    ADD_TO_CART_BTN = "[id^='add-to-cart']"
    REMOVE_BTN = ".btn_inventory[id^='remove']"
    BTN_ADD_OR_REMOVE = ".btn_inventory"
    PRODUCT_PRICE = ".inventory_item_price"
    SORT_SELECT = ".product_sort_container"
    CART_BTN = ".shopping_cart_link"

    def get_title_page(self):
        return self.get_text(self.TITLE_TEXT)

    def make_list_of_all_title_products(self):
        list_products =self.make_list(self.PRODUCT_AREA)
        count = list_products.count()
        list_title_products = []
        for i in range(count):
            list_title_products.append(self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE))
        return list_title_products

    def open_cart(self):
        self.click(self.CART_BTN)

    def enter_to_page_product(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE)==product_name:
                self.click_locator_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE)
                break


    def add_to_cart_product(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE)==product_name:
                self.click_locator_in_list(self.PRODUCT_AREA,i,self.ADD_TO_CART_BTN)
                break

    def remove_product(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE)==product_name:
                self.click_locator_in_list(self.PRODUCT_AREA,i,self.REMOVE_BTN)
                break

    def get_price_text(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE) == product_name:
                price_text =self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE)
                return price_text

    def get_price_as_num(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE) == product_name:
                price_text =self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE)
                price_as_num =float(price_text.replace("$",""))
                return price_as_num

    def get_product_desc(self,product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE) == product_name:
                desc =self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_DESC_TEXT)
                return desc

    def get_text_in_add_btn(self , product_name):
        product_list = self.make_list(self.PRODUCT_AREA)
        count = product_list.count()
        for i in range(count):
            if self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE) == product_name:
                text_in_btn = self.get_text_in_list(self.PRODUCT_AREA, i, self.BTN_ADD_OR_REMOVE)
                return text_in_btn

    def select_filter(self, az_za_lohi_hilo):
        if az_za_lohi_hilo in ("az", "za", "lohi", "hilo"):
            self.select_option(self.SORT_SELECT, az_za_lohi_hilo)
        else:
            print("not option for choice")

    def get_text_in_filter(self):
        text_filter = self.get_chose_text_in_select(self.SORT_SELECT)
        return text_filter

    def get_value_in_filter(self):
        value_filter = self.get_chose_value_in_select(self.SORT_SELECT)
        return value_filter

    def is_order_correct(self, az_za_lohi_hilo):
        correct = True
        products = self.make_list(self.PRODUCT_AREA)
        count = products.count()
        match az_za_lohi_hilo:
            case "az":
                product_name = self.get_text_in_list(self.PRODUCT_AREA,0,self.PRODUCT_TITLE)
                for i in range(count):
                   if self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE) >= product_name:
                       product_name = self.get_text_in_list(self.PRODUCT_AREA,i,self.PRODUCT_TITLE)
                   else:
                       return False
            case "za":
                product_name = self.get_text_in_list(self.PRODUCT_AREA,0,self.PRODUCT_TITLE)
                for i in range(count):
                    if self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE) <= product_name:
                        product_name = self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_TITLE)
                    else:
                        return False
            case "lohi":
                product_price = float(self.get_text_in_list(self.PRODUCT_AREA, 0, self.PRODUCT_PRICE).replace("$",""))
                for i in range(count):
                    if float(self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE).replace("$","")) >= product_price:
                        product_price = float(self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE).replace("$",""))
                    else:
                        return False
            case "hilo":
                product_price = float(self.get_text_in_list(self.PRODUCT_AREA, 0, self.PRODUCT_PRICE).replace("$",""))
                for i in range(count):
                    if float(self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE).replace("$","")) <= product_price:
                        product_price = float(self.get_text_in_list(self.PRODUCT_AREA, i, self.PRODUCT_PRICE).replace("$",""))
                    else:
                        return False
            case _:
                print("not option for choice")
                return False
        return correct
