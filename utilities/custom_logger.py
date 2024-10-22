import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    # following line gets the name of the class/method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = logging.FileHandler(
            r"C:\Users\omerfatih.poyraz\workspace_python\BehaveBDDFrameworkPOM\logs\automation.log", mode="a")
        file_handler.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s: -%(name)s - %(levelname)s: %(message)s ",
                                      datefmt="%m/%d/%Y %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
