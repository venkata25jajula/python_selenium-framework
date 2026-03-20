import os
from datetime import datetime
import allure
import pytest


class PytestHooks:

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()

        if report.when == "call" and report.failed:

            driver = None

            if hasattr(item, "instance") and item.instance:
                driver = getattr(item.instance, "driver", None)

            if driver:
                os.makedirs("screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
                driver.save_screenshot(screenshot_path)

                allure.attach.file(
                    screenshot_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

                print(f"Screenshot saved: {screenshot_path}")

def pytest_configure(config):
    config.pluginmanager.register(PytestHooks(), "pytest-hooks")
