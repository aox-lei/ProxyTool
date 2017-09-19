import logging
from datetime import datetime
from pymongo import MongoClient
from app.util.config import config


class init(object):
    _init = {}

    def __init__(self, env=''):
        if env == '' and 'env' in self._init:
            env = self._init.get('env')

        self._init_config(env)
        self._init_logging()
        self._init_mongo()

    def _init_config(self, env):
        config(env)

    def _init_logging(self):
        logger = logging.getLogger()
        # filename = 'log/info-%s.log' % (datetime.now().strftime('%Y-%m-%d'))
        #
        # file_handle = logging.FileHandler(filename, mode='a')
        format_handle = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d](FunctionName:%(funcName)s) %(levelname)s %(message)s')
        # file_handle.setFormatter(format_handle)
        # logger.setLevel(logging.INFO)
        # logger.addHandler(file_handle)

        if config().debug == 1:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(format_handle)
            logger.addHandler(console_handle)

    def _init_mongo(self):
        if 'db' not in self._init:
            client = MongoClient(config().mongo_dsn, connect=False)
            self._init['db'] = client[config().mongo_db]

    def __getattr__(self, key):
        if key in self._init:
            return self._init.get(key)
        return None
