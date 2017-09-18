import logging
from datetime import datetime
from app.util.config import config


class log(object):
    def write(self, type='info', msg=''):
        logger = logging.getLogger()
        filename = 'log/%s_%s.log' % (type, datetime.now().strftime('%Y-%m-%d'))

        file_handle = logging.FileHandler(filename, mode='a')
        format_handle = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s %(message)s')
        file_handle.setFormatter(format_handle)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handle)

        if config().debug == 1:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(format_handle)
            logger.addHandler(console_handle)

        if type == 'debug':
            logger.debug(msg)
        elif type == 'warning':
            logger.warning(msg)
        elif type == 'info':
            logger.info(msg)
