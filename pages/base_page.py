from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utils.logger import LogGen


class BasePage:

    logger = LogGen.get_logger("BasePage")

    PAGE_TITLE = (By.XPATH, "//span[@class='title']")

    def __init__(self, driver, testname):
        self.driver = driver
        self.testname = testname
        self.wait = WebDriverWait(driver, 20)

    # ---------- Element Finders ----------

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # ---------- Element Actions ----------

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.logger.info(f"Clicked on element : {locator}", extra={"testname": self.testname})

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text <<{text}>> into element with locator: {locator}", extra={"testname": self.testname})

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.logger.info(f"Text from element {locator} :  <<{element.text}>>", extra={"testname": self.testname})
        return element.text

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    # ---------- Wait Helpers ----------

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # ---------- Dropdown ----------

    def select_by_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)
        self.logger.info(f"Selected '{text}' from dropdown with locator: {locator}", extra={"testname": self.testname})

    # ---------- Mouse Actions ----------

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        self.logger.info(f"Hovered over element : {locator}", extra={"testname": self.testname})

    # ---------- Alerts ----------

    def accept_alert(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
            self.logger.info("Alert accepted", extra={"testname": self.testname})
        except TimeoutException:
            self.logger.info("No alert present", extra={"testname": self.testname})

    def dismiss_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
        self.logger.info("Alert dismissed", extra={"testname": self.testname})

    # ---------- Page Info ----------

    def get_title(self):
        self.logger.info(f"Current page title: <<{self.driver.title}>>", extra={"testname": self.testname})
        return self.driver.title

    def get_current_url(self):
        self.logger.info(f"Current URL: <<{self.driver.current_url}>>", extra={"testname": self.testname})
        return self.driver.current_url

    # ---------- Custom Methods for Application ----------
    def get_badge_count(self, CART_BADGE):
        try:
            badge = self.find_element(CART_BADGE)
            self.logger.info(f"Cart badge count: {badge.text}", extra={"testname": self.testname})
            return int(badge.text)
        except:
            return 0

    def get_page_title(self, page_name):
        # Add waiting for the page title element to be visible before trying to get its text
        self.wait_for_visible(self.PAGE_TITLE)
        page_title = self.get_text(self.PAGE_TITLE)
        self.logger.info(f"Getting {page_name} : {page_title}", extra={"testname": self.testname})
        return page_title

