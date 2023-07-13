from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys

logging.info('Welcome to this project')

try:
    a = 5/"y"
except Exception as e:
    raise AppException(e, sys)
