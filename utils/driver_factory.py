from abc import ABC, abstractmethod
from enum import Enum

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class IDriverStrategy(ABC):
    @abstractmethod
    def create_driver(self):
        pass


class ChromeDriverStrategy(IDriverStrategy):
    def create_driver(self):

        chrome_options = Options()
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False
            }
        )
        driver = webdriver.Chrome(options=chrome_options)

        return driver


class FirefoxDriverStrategy(IDriverStrategy):
    def create_driver(self):
        from selenium import webdriver
        return webdriver.Firefox()


class EdgeDriverStrategy(IDriverStrategy):
    def create_driver(self):
        from selenium import webdriver
        return webdriver.Edge()


class Browser(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"


class DriverFactory:
    def __init__(self, strategy: IDriverStrategy):
        self.strategy = strategy

    def get_driver(self):
        return self.strategy.create_driver()

    @staticmethod
    def get_driver_strategy(browser: Browser):
        if browser == Browser.CHROME:
            return ChromeDriverStrategy()

        elif browser == Browser.FIREFOX:
            return FirefoxDriverStrategy()

        elif browser == Browser.EDGE:
            return EdgeDriverStrategy()
        else:
            raise ValueError("Unsupported browser")
