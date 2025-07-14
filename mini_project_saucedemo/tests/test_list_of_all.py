import pytest
from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.InformationPage import InformationPage
from mini_project_saucedemo.pages.cartPage import CartPage
from mini_project_saucedemo.pages.checkoutPage import CheckoutPage
from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_List_of_all(Base_test):
        def test_of_all_list(self):
                self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
                list_products = self.productsPage.make_list_of_all_title_products()
                list_desc_products = []
                for product in list_products:
                    self.productsPage.add_to_cart_product(product)
                    list_desc_products.append(self.productsPage.get_product_desc(product))
                self.productsPage.open_cart()
                list_items = self.cartPage.make_string_list_of_names_items()
                list_desc_cart_items = []
                for item in list_items:
                    list_desc_cart_items.append(self.cartPage.return_descriptions_item(item))
                self.cartPage.continue_shopping()
                list_inner_desc = []
                for product in list_products:
                        self.productsPage.enter_to_page_product(product)
                        list_inner_desc.append(self.productPage.get_desc())
                        self.productPage.click_btn_add_or_remove()
                        self.productPage.bake_to_products()
                list_products = self.productsPage.make_list_of_all_title_products()
                for product in list_products:
                        self.productsPage.add_to_cart_product(product)
                self.productsPage.open_cart()
                self.cartPage.checkout()
                self.informationPage.fill_information_and_continue("aaa","bbb0","5326980")
                list_desc_checkout = []
                list_checkout_items = self.checkoutPage.make_title_list()
                for item in list_checkout_items:
                        list_desc_checkout.append(self.checkoutPage.get_desc(item))
                self.checkoutPage.finish()
                assert list_desc_cart_items==list_desc_products==list_inner_desc==list_desc_checkout