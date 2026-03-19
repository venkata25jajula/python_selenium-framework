import allure

from tests.base_test import BaseTest
from utils.logger import LogGen
from utils.page_factory import PageFactory


@allure.feature("Inventory Tests")
class TestInventory(BaseTest):

    logger = LogGen.get_logger("TestInventory")

    @allure.story("Verify inventory page")
    def test_inventory(self):
        with allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_inventory").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
        with allure.step("Verify inventory page title"):
            expected_page_title = "Products"
            actual_page_title = inventory_page.get_page_title("Inventory Page Title")
        with allure.step("Verify inventory page URL"):
            current_url = inventory_page.get_current_url()
            expected_url = "https://www.saucedemo.com/inventory.html"
        with allure.step("Get inventory items list"):
            inventory_items = inventory_page.get_inventory_items()
        with allure.step("Validate page title"):
            assert expected_page_title in actual_page_title, self.logger.error(f"Expected page title to contain: <<{expected_page_title}>>, but got: <<{actual_page_title}>>", extra={"testname": self.testname})
        with allure.step("Validate inventory page URL"):
            assert current_url == expected_url, self.logger.error(f"Expected URL: <<{expected_url}>>, but got: <<{current_url}>>", extra={"testname": self.testname})
        with allure.step("Validate inventory items count"):
            assert len(inventory_items) == 6, self.logger.error(f"Expected 6 inventory items, but found: <<{len(inventory_items)}>>", extra={"testname": self.testname})

    @allure.story("Add items to cart and verify badge count in Inventory Page")
    def test_add_item_to_cart(self):

        with allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_add_item_to_cart").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
            inventory_page.get_inventory_items()
        with allure.step("Add items to cart and verify badge count"):
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        with allure.step("Get cart badge count and validate with cart items count"):
            expected_cart_badge_count = inventory_page.get_badge_count(inventory_page.CART_BADGE)
            assert expected_cart_badge_count == 2, self.logger.error("Cart badge count should be 2 after adding an item to the cart", extra={"testname": self.testname})




