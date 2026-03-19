from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import LogGen
from utils.page_factory import PageFactory


class CartPage(BasePage):

    logger = LogGen.get_logger("CartPage")

    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    ITEM_LINK = "item_{}_title_link"
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver, testname):
        super().__init__(driver, testname)

    def get_cart_items(self):

        items = []
        # Select all item names in the cart
        cart_item_elements = self.find_elements(self.ITEM_NAME)
        for element in cart_item_elements:
            item_name = element.text
            items.append(item_name)
            self.logger.info(f"Cart item: <<{item_name}>>", extra={"testname": self.testname})

        return items


    def proceed_to_checkout(self):
        # Implement logic to click on the checkout button
        self.click(self.CHECKOUT_BUTTON)
        return PageFactory(self.driver, self.testname).get_checkout_page()

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)
        return PageFactory(self.driver, self.testname).get_inventory_page()



