from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import LogGen
from utils.page_factory import PageFactory


class PaymentPage(BasePage):

    logger = LogGen.get_logger("PaymentPage")

    # Define locators for payment page elements

    PAYMENT_INFO = (By.ID, "payment-info")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver, testname):
       super().__init__(driver, testname)

    def verify_payment_info(self):
        # Implement logic to verify payment information
        return self.is_element_present(self.PAYMENT_INFO)

    def finish_payment(self):
        self.click(self.FINISH_BUTTON)
        return PageFactory(self.driver, self.testname).get_confirmation_page()

    def get_payment_title(self):
        return self.get_text(self.PAYMENT_TITLE)


