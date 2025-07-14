from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.InformationPage import InformationPage
from mini_project_saucedemo.pages.basePage import BasePage
from mini_project_saucedemo.pages.cartPage import CartPage
from mini_project_saucedemo.pages.checkoutPage import CheckoutPage
from mini_project_saucedemo.pages.completePage import CompletePage
from mini_project_saucedemo.pages.envelopePage import EnvelopePage
from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from utils.config import ConfigReader


class Base_test:
        #pages:
        basePade: BasePage
        cartPage: CartPage
        checkoutPage: CheckoutPage
        completePage: CompletePage
        informationPage: InformationPage
        loginPage: LoginPage
        productPage: ProductPage
        productsPage: ProductsPage
        envelopePage: EnvelopePage

        #start:
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False, slow_mo=300, args=["--start-maximized"])
        #page = browser.new_page()

        #data:
        data_url:str
        data_user_name:str
        data_password:str
        data_product_1:str
        data_product_2:str


#
        def set_slow_mo(self,slow_mo):
            #מתודה לצורת עבודה בה נרצה לשלוט במהירות בנפרד , תקבל את הP מהשורות בהערה בראשית הקלאס
            page = self.p.chromium.launch(headless=False, slow_mo=slow_mo, args=["--start-maximized"]).new_page()
            return page


