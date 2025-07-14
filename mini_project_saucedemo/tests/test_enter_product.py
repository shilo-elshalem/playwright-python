# start and login:
import pytest
from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_enter_product(Base_test):
    @pytest.mark.dependency()
    def test_enter_product(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        self.productsPage.enter_to_page_product(self.data_product_1)
        #A place to demonstrate failure and subsequent jump - placing data_product_2 instead of data_product_1
        assert self.productPage.get_name_product()==self.data_product_2  ,'is not equal'

    @pytest.mark.dependency(depends=["Test_enter_product::test_enter_product"])
    def test_enter_to_all_products(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        is_succeeded = True
        products = self.productsPage.make_list_of_all_title_products()
        for title in products:
            self.productsPage.enter_to_page_product(title)
            is_succeeded=is_succeeded and self.productPage.get_name_product() == title
            self.productPage.bake_to_products()
        assert is_succeeded


