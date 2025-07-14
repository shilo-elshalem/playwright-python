import pytest
from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_price_and_order_product(Base_test):
    def test_price_for_product(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        assert 29.99 ==self.productsPage.get_price_as_num("Sauce Labs Backpack")

    def test_order_lohi(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("lohi")
        assert self.productsPage.is_order_correct("lohi")

    def test_text_lohi(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("lohi")
        assert self.productsPage.get_text_in_filter()=="Price (low to high)"

    def test_order_az(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("az")
        assert self.productsPage.is_order_correct("az")

    def test_text_az(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("az")
        assert self.productsPage.get_text_in_filter() == "Name (A to Z)"

    def test_order_za(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("za")
        assert self.productsPage.is_order_correct("za")

    def test_text_za(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("za")
        assert self.productsPage.get_text_in_filter() == "Name (Z to A)"

    def test_order_hilo(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("hilo")
        assert self.productsPage.is_order_correct("hilo")

    def test_text_hilo(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.select_filter("hilo")
        assert self.productsPage.get_text_in_filter() == "Price (high to low)"








