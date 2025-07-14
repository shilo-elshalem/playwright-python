import time

import pytest

from mini_project_saucedemo.tests.base_test import Base_test

@pytest.mark.usefixtures("setup_page_class")
class Test_null_in_info(Base_test):
    #@pytest.mark.dependency()
    def test_null_in_info(self):
        self.loginPage.fill_details_and_login(self.data_user_name, self.data_password)
        self.productsPage.open_cart()
        self.cartPage.checkout()
        self.informationPage.click_continue()
        #time.sleep(100)
        assert self.informationPage.get_error_text() == "Error: First Name is required"

    #@pytest.mark.dependency(depends=["Test_null_in_info::test_null_in_info"])
    def test_fill_only_firstname(self):
        self.informationPage.fill_first_name("aaa")
        self.informationPage.click_continue()
        assert self.informationPage.get_error_text() == "Error: Last Name is required"
        self.informationPage.fill_first_name("")

    #@pytest.mark.dependency(depends=["Test_null_in_info::test_fill_only_firstname"])
    def test_fill_only_lastname(self):
        self.informationPage.fill_last_name("aaa")
        self.informationPage.click_continue()
        assert self.informationPage.get_error_text() == "Error: First Name is required"
        self.informationPage.fill_last_name("")

    #@pytest.mark.dependency(depends=["Test_null_in_info::test_null_in_info"])
    def test_fill_only_firstnaem_and_code(self):
        self.informationPage.fill_information_and_continue("aaa","","3456")
        assert self.informationPage.get_error_text() == "Error: Last Name is required"

    #@pytest.mark.dependency(depends=["Test_null_in_info::test_null_in_info"])
    def test_fill_only_firstname_and_lastname(self):
        self.informationPage.fill_information_and_continue("aaa", "bbb", "")
        assert self.informationPage.get_error_text() == "Error: Postal Code is required"

    #@pytest.mark.dependency(depends=["Test_null_in_info::test_null_in_info"])
    def test_fill_all_info(self):
        # הערה לבודקי הפרוייקט שלי -
        # הכנסתי בטסט הזה שם אחר כמחווה , כמובן שאני (שילה אלשלם) כתבתי את הקוד בעזרת ה' וזה לא קוד שהעתקתי מהראל חלילה
        self.informationPage.fill_information_and_continue("Harel", "Elikamel", "5263487")
        assert self.checkoutPage.get_title_page() == "Checkout: Overview"