from loguru import logger

logger.add("logs/logs.log", format="{time} {level} {message}", level="DEBUG", rotation="1 MB")


def add_log(message: str, level: str):
    if level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    elif level == "ERROR":
        logger.error(message)
    elif level == "CRITICAL":
        logger.critical(message)

