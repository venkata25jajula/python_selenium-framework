import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import LogGen
from utils.page_factory import PageFactory


class LoginPage(BasePage):

    logger = LogGen.get_logger("LoginPage")

    def __init__(self, driver, testname):
        super().__init__(driver, testname)


    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
        self.logger.info(f"Username entered:<<{username}>>", extra={"testname":self.testname})

    @allure.step("Enter password: {password}")
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
        self.logger.info(f"Password entered:<<{password}>>", extra={"testname":self.testname})

    @allure.step("Click on Login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Login Button clicked", extra={"testname":self.testname})

    def login(self, username, password):
        """Business action method"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        return PageFactory(self.driver, self.testname).get_inventory_page()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
