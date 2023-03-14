import logging
from pathlib import Path

def custom_logger():
    # Create a customer logger
    logger = logging.getLogger(__name__)
    # Create a handler
    file_name = 'log.txt'
    file_name.tou


    file_handler = logging.FileHandler(filename='test.txt', mode='r')
    file_handler.setLevel(logging.DEBUG)
    # Create a file formatter
    file_fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
    file_handler.setFormatter(file_fmt)
    # Add handler to logger
    logger.addHandler(file_handler)

    return logger