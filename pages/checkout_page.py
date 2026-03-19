from pages.base_page import BasePage
from utils.logger import LogGen
from utils.page_factory import PageFactory


class CheckoutPage(BasePage):

    logger = LogGen.get_logger("CheckoutPage")
    # Define locators for checkout information fields
    FIRST_NAME_INPUT = ("id", "first-name")
    LAST_NAME_INPUT = ("id", "last-name")
    POSTAL_CODE_INPUT = ("id", "postal-code")
    CONTINUE_BUTTON = ("id", "continue")

    def __init__(self, driver, testname):
        super().__init__(driver, testname)

    def input_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def input_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def input_postal_code(self, postal_code):
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)

    def enter_checkout_information(self, first_name, last_name, postal_code):
        # Implement logic to enter checkout information
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_postal_code(postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        return PageFactory(self.driver, self.testname).get_payment_page()
