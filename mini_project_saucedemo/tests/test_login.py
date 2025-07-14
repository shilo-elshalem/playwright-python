import pytest
from playwright.sync_api import sync_playwright

from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_function")
class Test_login(Base_test):
    def test_login(self):
        self.loginPage.fill_details_and_login(self.data_user_name,self.data_password)
        assert self.productsPage.get_title_page()=="Products"

    def test_invalid_password(self):
        self.loginPage.fill_details_and_login(self.data_user_name, "jjjjjj")
        assert self.loginPage.get_error() == "Epic sadface: Username and password do not match any user in this service"

    def test_invalid_user_name(self):
        self.loginPage.fill_details_and_login("edfgbnh",self.data_password)
        assert self.loginPage.get_error() == "Epic sadface: Username and password do not match any user in this service"

    def test_login_without_details(self):
        self.loginPage.click_btn_login()
        assert self.loginPage.get_error() == "Epic sadface: Username is required"

    def test_login_without_password(self):
        self.loginPage.fill_user_name(self.data_user_name)
        self.loginPage.click_btn_login()
        assert self.loginPage.get_error() == "Epic sadface: Password is required"

    def test_login_without_password_with_invalid_user_name(self):
        self.loginPage.fill_user_name("jjuuhhygg")
        self.loginPage.click_btn_login()
        assert self.loginPage.get_error() == "Epic sadface: Password is required"

    def test_open_and_close_error(self):
        is_passed = self.loginPage.get_error() == ""
        self.loginPage.click_btn_login()
        is_passed = is_passed and self.loginPage.get_error()=="Epic sadface: Username is required"
        self.loginPage.close_error()
        is_passed = is_passed and self.loginPage.get_error() == ""
        assert is_passed
