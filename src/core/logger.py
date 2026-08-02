import logging
from logging.handlers import RotatingFileHandler

# log path
from core.constants import LOG_PATH


formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(message)s'
)


def setup_logger(name, file_name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        LOG_PATH / file_name,
        maxBytes=5_000_000,
        backupCount=5,
        encoding='utf-8'
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def addlog(name, message):
    """Adiciona a mensagem ao logs do bot"""
    
    logger = setup_logger(name, f'{name}.log')

    if name == 'error':
        logger.error(message)
    else:
        logger.info(message)
