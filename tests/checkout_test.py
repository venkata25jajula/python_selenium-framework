import allure

from tests.base_test import BaseTest
from utils.page_factory import PageFactory


@allure.feature("Checkout Tests")
class TestCheckout(BaseTest):

    @allure.story("Verify checkout process from cart to order confirmation")
    def test_checkout(self):

        with allure.step("Open login page and login with valid credentials"):
            login_page = PageFactory(self.driver, "test_checkout").get_login_page()
            inventory_page = login_page.login("standard_user", "secret_sauce")
        with allure.step("Add items to cart and proceed to checkout"):
            inventory_page.add_item_to_cart("Sauce Labs Backpack")
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
        with allure.step("Go to cart page"):
            cart_page = inventory_page.go_to_cart()
        with allure.step("Proceed to checkout page"):
            checkout_page = cart_page.proceed_to_checkout()
        with allure.step("Verify checkout page title"):
            checkout_page_expected_title = "Checkout: Your Information"
            checkout_page_actual_title = checkout_page.get_page_title("Checkout Page Title")
            assert checkout_page_expected_title in checkout_page_actual_title, f"Expected title: <<{checkout_page_expected_title}>>, but got: <<{checkout_page_actual_title}>>"

        with allure.step("Verify checkout page URL"):
            checkout_page_expected_url = "https://www.saucedemo.com/checkout-step-one.html"
            checkout_page_actual_url = checkout_page.get_current_url()
            assert checkout_page_expected_url == checkout_page_actual_url, f"Expected URL: <<{checkout_page_expected_url}>>, but got: <<{checkout_page_actual_url}>>"

        with allure.step("Enter checkout information"):
            checkout_page.enter_checkout_information("John", "Doe", "12345")

        with  allure.step("Continue to payment page"):
            payment_page = checkout_page.continue_checkout()

        with allure.step("Verify payment page title"):
            payment_page_expected_title = "Checkout: Overview"
            payment_page_actual_title = payment_page.get_page_title("Payment Page Title")
            assert payment_page_expected_title in payment_page_actual_title, f"Expected title: <<{payment_page_expected_title}>>, but got: <<{payment_page_actual_title}>>"
        with allure.step("Verify payment page URL"):
            payment_expected_url = "https://www.saucedemo.com/checkout-step-two.html"
            payment_page_actual_url = payment_page.get_current_url()
            assert payment_expected_url == payment_page_actual_url, f"Expected URL: <<{payment_expected_url}>>, but got: <<{payment_page_actual_url}>>"
        with allure.step("Click Finish payment button"):
            confirmation_page = payment_page.finish_payment()
        with allure.step("Verify order confirmation page title"):
            confirmation_page_expected_title = "Checkout: Complete!"
            confirmation_page_actual_title = confirmation_page.get_page_title("Confirmation Page Title")
            assert confirmation_page_expected_title in confirmation_page_actual_title, f"Expected title: <<{confirmation_page_expected_title}>>, but got: <<{confirmation_page_actual_title}>>"

        with allure.step("Verify order confirmation page URL"):
            confirmation_page_expected_url = "https://www.saucedemo.com/checkout-complete.html"
            confirmation_page_actual_url = confirmation_page.get_current_url()
            assert confirmation_page_expected_url == confirmation_page_actual_url, f"Expected URL: <<{confirmation_page_expected_url}>>, but got: <<{confirmation_page_actual_url}>>"

        with allure.step("Verify order confirmation message"):
            expected_confirmation_message = "Thank you for your order!"
            actual_confirmation_message = confirmation_page.get_confirmation_message()
            assert expected_confirmation_message == actual_confirmation_message, f"Expected confirmation message: <<{expected_confirmation_message}>>, but got: <<{actual_confirmation_message}>>"



