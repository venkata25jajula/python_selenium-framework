from datetime import datetime
import logging
import os

from utils.utilities import Utilities


class LogGen:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(Utilities.get_project_path(), "logs", f"automation_{timestamp}.log")

    @staticmethod
    def get_logger(name, testname=None):
        log_dir = os.path.dirname(LogGen.log_file)
        os.makedirs(log_dir, exist_ok=True)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        logger.propagate = False

        if not logger.handlers:
            file_handler = logging.FileHandler(LogGen.log_file)
            console_handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(module)s | %(name)s | %(testname)s | %(message)s"
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
