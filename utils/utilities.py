import os


class Utilities:

    @staticmethod
    def get_project_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

