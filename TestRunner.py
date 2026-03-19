import pytest
import sys


class TestRunner:

    @staticmethod
    def run_tests():
        pytest_args = [
            "tests",  # test folder
            "-v",  # verbose
            "--alluredir=reports/allure-results",
            "--clean-alluredir"
        ]
        result = pytest.main(pytest_args)
        sys.exit(result)


if __name__ == "__main__":
    TestRunner.run_tests()
