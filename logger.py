import logging


def setup_logger():
    logger = logging.getLogger("tests")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    logger.addHandler(console_handler)

    return logger
