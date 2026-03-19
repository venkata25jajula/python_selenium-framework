from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import LogGen


class ConfirmationPage(BasePage):

    logger = LogGen.get_logger("ConfirmationPage")

    # Define locators for confirmation page elements
    CONFIRM_MESSAGE = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver, testname):
        super(ConfirmationPage, self).__init__(driver, testname)

    def get_confirmation_message(self):
        # Implement logic to retrieve the confirmation message
        return self.get_text(self.CONFIRM_MESSAGE)

    def go_back_home(self):
        self.click(self.BACK_HOME_BUTTON)




