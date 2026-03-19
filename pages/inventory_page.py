from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import LogGen
from utils.page_factory import PageFactory


class InventoryPage(BasePage):
    logger = LogGen.get_logger("InventoryPage")

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = "//div[normalize-space()='{}']/ancestor::div[@class='inventory_item']//button"
    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, testname):
        super().__init__(driver, testname)

    def get_inventory_items(self):
        # Implement logic to retrieve inventory items from the page
        items = self.find_elements(self.INVENTORY_ITEMS)
        item_names = [item.text for item in items]
        self.logger.info(f"Inventory items: {item_names}", extra={"testname": self.testname})

        return item_names

    def add_item_to_cart(self, item_name):
        # Implement logic to add a specific item to the cart
        item_locator = (By.XPATH, self.ADD_TO_CART_BUTTON.format(item_name))
        # print(item_locator)
        self.click(item_locator)

    def add_item_to_cart_new(self, item_name):
        item_id = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{item_id}")
        self.click(locator)

    def remove_item_from_cart(self, item_name):
        # Implement logic to remove a specific item from the cart
        pass

    def get_cart_items(self):
        # Implement logic to retrieve items currently in the cart
        cart_items = []
        items = self.find_elements(self.INVENTORY_ITEMS)
        item_names = [item.text for item in items]
        self.logger.info(f"Inventory items: {item_names}", extra={"testname": self.testname})

    def go_to_cart(self):
        self.click(self.CART_LINK)
        return PageFactory(self.driver, self.testname).get_cart_page()
