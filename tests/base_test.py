import time
import allure
import pytest
from configs.config_reader import ConfigReader
from utils.driver_factory import DriverFactory, Browser
from utils.logger import LogGen


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.testname = request.node.name
        self.logger = LogGen.get_logger(self.__class__.__name__, self.testname)

        self.configreader = ConfigReader()
        browser_name = self.configreader.get_browser()
        base_url = self.configreader.get_base_url()
        browser = Browser(browser_name)

        strategy = DriverFactory.get_driver_strategy(browser)
        factory = DriverFactory(strategy)
        with allure.step(f"Starting Test {self.testname} "):
            self.logger.info(f"Starting Test {self.testname} " ,extra={"testname": self.testname})
        with allure.step(f"Initializing WebDriver for {browser_name}"):
            self.driver = factory.get_driver()
        with allure.step(f"Launching application in {browser_name} using URL {base_url}"):
            self.driver.get(base_url)
            self.logger.info(f"launch application in {browser_name} chrome using URL {base_url}", extra={"testname": self.testname})
        with allure.step("Maximizing the browser window and setting implicit wait"):
            self.driver.maximize_window()
            self.logger.info(f"Maximize the window", extra={"testname": self.testname})
            self.driver.implicitly_wait(10)

        yield
        time.sleep(2)  # Optional: Add a small wait before quitting the driver
        with allure.step("Quitting the WebDriver"):
            self.driver.quit()
        with allure.step(f"Finished Test {self.testname}"):
            self.logger.info(f"Finished test {self.testname}", extra={"testname": self.testname})

