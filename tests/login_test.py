import allure
from tests.base_test import BaseTest
from utils.logger import LogGen
from utils.page_factory import PageFactory


@allure.feature("Login Tests")
class TestLogin(BaseTest):

    logger = LogGen.get_logger("TestLogin")

    @allure.story("Valid Login")
    def test_valid_login(self):
        with allure.step("Initialize login page"):
            login_page = PageFactory(self.driver,  "test_valid_login").get_login_page()
        with allure.step("Perform login with valid credentials"):
            login_page.login("standard_user", "secret_sauce")
        expected_title = "Swag Labs"
        with allure.step("Verify page title after login"):
            try:
                assert expected_title in self.driver.title
                self.logger.info(f"Assertion Passed: <<{expected_title}>> is present in the page title", extra={"testname": self.testname})
            except AssertionError:
                self.logger.error(f"Assertion Failed: <<{expected_title}>> NOT found in the page title. Actual title: <<{self.driver.title}>>'", extra={"testname": self.testname})
                raise  # re-raise to let pytest mark the test as failed

    @allure.story("Invalid Login")
    def test_invalid_login(self):
        with allure.step("Initialize login page"):
            login_page = PageFactory(self.driver,  "test_invalid_login").get_login_page()
        with allure.step("Perform login with invalid credentials"):
            login_page.login("standard_user", "secret_sauce1")
        with allure.step("Fetch error message"):
            expected_error = "Epic sadface: Username and password do not match any user in this service"
            actual_error = login_page.get_error_message()
            self.logger.info(f"Actual error message received: <<{actual_error}>>", extra={"testname": self.testname})
            assert expected_error == actual_error, self.logger.error(f"Expected error message: <<{expected_error}>>, but got: <<{actual_error}>>", extra={"testname": self.testname})

