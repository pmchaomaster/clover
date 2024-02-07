# Filename: utilities/logger.py

import logging
import os
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()

        # Set timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Create log file
        if not os.path.exists('logs'):
            os.makedirs('logs')
        file_handler = logging.FileHandler(f"logs/test_log_{timestamp}.log")

        # Set log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)
        return logger
