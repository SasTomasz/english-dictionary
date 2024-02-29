import logging
from logging.handlers import RotatingFileHandler
import sys


def set_base_logging():
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
    log_file = "./app_logs/logs.log"

    my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding='utf-8', delay=False)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.DEBUG)

    app_log = logging.getLogger('root')
    app_log.setLevel(logging.DEBUG)

    app_log.addHandler(my_handler)

    # Show logs in standard output
    app_log.addHandler(logging.StreamHandler(sys.stdout))
    return app_log
