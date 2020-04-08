import logging

FORMAT = '%(asctime)-15s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('converter')


def get_logger():
    return logger
