import pytest
from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.InformationPage import InformationPage
from mini_project_saucedemo.pages.basePage import BasePage
from mini_project_saucedemo.pages.cartPage import CartPage
from mini_project_saucedemo.pages.checkoutPage import CheckoutPage
from mini_project_saucedemo.pages.completePage import CompletePage
from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_e2e(Base_test):
    def test_e2e(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        self.productsPage.add_to_cart_product(self.data_product_1)
        self.productsPage.enter_to_page_product(self.data_product_2)
        self.productPage.add_to_cart()
        self.productPage.open_cart()
        self.cartPage.checkout()
        self.informationPage.fill_information_and_continue("aaa","bbb","ccc")
        self.checkoutPage.finish()
        self.completePage.click_bake_home()
        assert self.productsPage.get_title_page()=="Products"
