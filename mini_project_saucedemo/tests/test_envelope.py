from time import sleep

import pytest

from mini_project_saucedemo.pages.envelopePage import EnvelopePage
from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_Envelope(Base_test):
    def test_logout(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        self.envelopePage.open_menu_and_chose_logout()
        assert self.envelopePage.page.url == self.data_url

    def test_about(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        self.envelopePage.open_menu_and_chose_about()
        assert self.envelopePage.page.url == "https://saucelabs.com/"

    def test_products(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.open_cart()
        self.envelopePage.open_menu_and_chose_all_items()
        assert self.productsPage.get_title_page() == "Products"

    def test_reset(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.add_to_cart_product(self.data_product_1)
        self.productsPage.open_cart()
        assert self.cartPage.return_sum_items() == 1
        #Due to a problem on the site here, I had to leave the page, empty the cart outside, and then return.
        self.cartPage.continue_shopping()
        self.envelopePage.open_menu_and_chose_reset()
        self.productsPage.open_cart()
        assert self.cartPage.return_sum_items() == 0


    def test_open_twitter(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.envelopePage.open_twitter()
        assert self.envelopePage.get_url_new_tab() == "https://x.com/saucelabs"
        self.envelopePage.close_new_tab()

    def test_open_linkedin(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.envelopePage.open_linkedin()
        assert self.envelopePage.get_url_new_tab() == "https://www.linkedin.com/company/sauce-labs/"
        self.envelopePage.close_new_tab()

    def test_open_facebook(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.envelopePage.open_facebook()
        assert self.envelopePage.get_url_new_tab() == "https://www.facebook.com/saucelabs"
        self.envelopePage.close_new_tab()