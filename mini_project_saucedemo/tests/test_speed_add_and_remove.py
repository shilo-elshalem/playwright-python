import pytest
from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser

from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test
from utils.config import ConfigReader

@pytest.mark.usefixtures("setup_page_function")
class Test_speed_add_and_remove(Base_test):

    def test_speed_add_and_remove(self):
        page = self.set_slow_mo(0)
        # start and login:
        page.goto(self.data_url)
        loginPage = LoginPage(page)
        loginPage.fill_details_and_login(self.data_user_name, self.data_password)

        # main test:
        productsPage = ProductsPage(page)
        productsPage.enter_to_page_product(self.data_product_1)
        productPage = ProductPage(page)
        for i in range(30):
            productPage.click_btn_add_or_remove()
        print(productPage.get_text_in_btn())
        text_in_btn = productPage.get_text_in_btn()
        productPage.bake_to_products()
        for i in range (30):
            productsPage.add_to_cart_product(self.data_product_1)
            productsPage.remove_product(self.data_product_1)
        #print(productsPage.get_text_in_add_btn(self.data_product_1))
        assert "Add to cart" == text_in_btn == productsPage.get_text_in_add_btn(self.data_product_1)
        #page.close()
