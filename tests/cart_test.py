import allure

from tests.base_test import BaseTest
from utils.logger import LogGen
from utils.page_factory import PageFactory


@allure.feature("Cart Tests")
class TestCart(BaseTest):
    logger = LogGen.get_logger("TestCart")

    @allure.story("Verify cart page and URL after adding items to cart")
    def test_cart(self):
        with  allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_cart").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
        with allure.step("Add items to cart"):
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        with allure.step("Go to cart page"):
            cart_page = inventory_page.go_to_cart()
        with allure.step("Verify cart page title and URL"):
            expected_page_title = "Your Cart"
            actual_page_title = cart_page.get_page_title("Cart Page Title")
        assert expected_page_title in actual_page_title, self.logger.error(
            f"Expected page title to contain: <<{expected_page_title}>>, but got: <<{actual_page_title}>>",
            extra={"testname": self.testname})
        with allure.step("Verify cart page URL"):
            current_url = inventory_page.get_current_url()
            expected_url = "https://www.saucedemo.com/cart.html"
            assert current_url == expected_url, self.logger.error(
                f"Expected URL: <<{expected_url}>>, but got: <<{current_url}>>", extra={"testname": self.testname})

    @allure.story("Validate items in cart after adding items from inventory page")
    def test_validate_items_in_cart(self):
        with allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_validate_items_in_cart").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
        with allure.step("Add items to cart"):
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        with allure.step("Go to cart page and validate items in cart"):
            cart_page = inventory_page.go_to_cart()
            item_count = cart_page.get_badge_count(cart_page.CART_BADGE)
            self.logger.info(f"Number of items in the cart: <<{item_count}>>", extra={"testname": self.testname})
            cart_items = cart_page.get_cart_items()
            assert item_count == len(cart_items), self.logger.error(
                f"Expected {item_count} items in the cart, but found: <<{len(cart_items)}>>",
                extra={"testname": self.testname})
        with allure.step("Validate specific items in the cart"):
            assert "Sauce Labs Backpack" in cart_items, self.logger.error("Sauce Labs Backpack should be in the cart",
                                                                      extra={"testname": self.testname})
            self.logger.info(f"Sauce Labs Backpack present in cart", extra={"testname": self.testname})
            assert "Sauce Labs Fleece Jacket" in cart_items, self.logger.error(
                "Sauce Labs Fleece Jacket should be in the cart", extra={"testname": self.testname})
            self.logger.info(f"Sauce Labs Fleece Jacket present in cart", extra={"testname": self.testname})

    @allure.story("Validate Continue Shopping functionality from cart page")
    def test_continue_shopping(self):

        with allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_validate_items_in_cart").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
        with allure.step("Add items to cart"):
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        with allure.step("Go to cart page"):
            cart_page = inventory_page.go_to_cart()
        with allure.step("Click on Continue Shopping"):
            inventory_page = cart_page.continue_shopping()
        with allure.step("User should land on Inventory Page- Verify URL"):
            current_url = inventory_page.get_current_url()
            self.logger.info(f"Current URL after clicking Continue Shopping: <<{current_url}>>", extra={"testname": self.testname})
            expected_url = "https://www.saucedemo.com/inventory.html"
            assert current_url == expected_url, self.logger.error(f"Expected URL: <<{expected_url}>>, but got: <<{current_url}>>", extra={"testname": self.testname})
