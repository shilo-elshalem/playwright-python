import os
import shutil
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright, Page

from mini_project_saucedemo.pages.InformationPage import InformationPage
from mini_project_saucedemo.pages.cartPage import CartPage
from mini_project_saucedemo.pages.checkoutPage import CheckoutPage
from mini_project_saucedemo.pages.completePage import CompletePage
from mini_project_saucedemo.pages.envelopePage import EnvelopePage
from mini_project_saucedemo.pages.loginPage import LoginPage
from mini_project_saucedemo.pages.productPage import ProductPage
from mini_project_saucedemo.pages.productsPage import ProductsPage
from utils.config import ConfigReader

@pytest.fixture(scope="session", autouse=True)
def clear_allure_reports():
    """Clear Allure reports before test run"""
    script_path = Path(__file__).resolve()
    project_root = script_path.parents[2]
    allure_report_directory = project_root / "allure-results"
    if os.path.exists(allure_report_directory):
        for filename in os.listdir(allure_report_directory):
            file_path = os.path.join(allure_report_directory, filename)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
            except Exception as e:
                pass

@pytest.fixture(scope="class")
def setup_page_class(request):
    #p = sync_playwright().start()
    #browser = p.chromium.launch(headless=False, slow_mo=250, args=["--start-maximized"])
    #request.cls.page.close()
    page = request.cls.browser.new_page()

    #data:
    request.cls.data_url = ConfigReader.read_config("general", "url")
    request.cls.data_user_name = ConfigReader.read_config("general", "user_name")
    request.cls.data_password = ConfigReader.read_config("general", "password")
    request.cls.data_product_1 = ConfigReader.read_config("products", "name_1")
    request.cls.data_product_2 = ConfigReader.read_config("products", "name_2")
    #pages:
    page.goto(request.cls.data_url)
    request.cls.cartPage = CartPage(page)
    request.cls.checkoutPage = CheckoutPage(page)
    request.cls.completePage = CompletePage(page)
    request.cls.informationPage = InformationPage(page)
    request.cls.loginPage = LoginPage(page)
    request.cls.productPage = ProductPage(page)
    request.cls.productsPage = ProductsPage(page)
    request.cls.envelopePage = EnvelopePage(page)
    yield
    page.close()
    #request.cls.page.close()
    #request.cls.browser.close()


@pytest.fixture(scope="function")
def setup_page_function(request):
    #p = sync_playwright().start()
    #browser = p.chromium.launch(headless=False, slow_mo=250, args=["--start-maximized"])
    page = request.cls.browser.new_page()

    #data:
    request.cls.data_url = ConfigReader.read_config("general", "url")
    request.cls.data_user_name = ConfigReader.read_config("general", "user_name")
    request.cls.data_password = ConfigReader.read_config("general", "password")
    request.cls.data_product_1 = ConfigReader.read_config("products", "name_1")
    request.cls.data_product_2 = ConfigReader.read_config("products", "name_2")
    #pages:
    page.goto(request.cls.data_url)
    request.cls.cartPage = CartPage(page)
    request.cls.checkoutPage = CheckoutPage(page)
    request.cls.completePage = CompletePage(page)
    request.cls.informationPage = InformationPage(page)
    request.cls.loginPage = LoginPage(page)
    request.cls.productPage = ProductPage(page)
    request.cls.productsPage = ProductsPage(page)
    request.cls.envelopePage = EnvelopePage(page)
    yield
    page.close()
    #request.cls.page.close()
    #request.cls.page = request.cls.browser.new_page()
    #request.cls.browser.close()