import logging


def setup_logger():
    logger = logging.getLogger("tests")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
                                  datefmt="%H:%M:%S")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
