import configparser
from pathlib import Path


class ConfigReader:

    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path(__file__).resolve().parent / "config.ini"
        self.config.read(config_path)
        print(self.config)              # object
        print(self.config.sections())   # should show ['settings']

    def get_browser(self):
        print(self.config)
        return self.config.get("settings", "browser")

    def get_base_url(self):
        return self.config.get("settings", "base_url")

    def get_implicit_wait(self):
        return self.config.getint("settings", "implicit_wait")
