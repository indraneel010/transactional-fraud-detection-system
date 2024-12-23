# utils/logger.py
"""
Logger module for recording system activity and errors.
"""

import logging
from config import LOG_LEVEL, LOG_FILE

def setup_logger():
    """
    Setup the logging configuration.
    """
    logging.basicConfig(
        filename=LOG_FILE,
        level=LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log(message, level="INFO"):
    """
    Log a message at the specified log level.
    :param message: The message to log.
    :param level: The level at which to log the message.
    """
    setup_logger()
    if level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    else:
        logging.debug(message)
