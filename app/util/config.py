import os
import json


class config(object):
    path = '../.env'
    config = {}

    def __init__(self):
        if len(self.config) == 0:
            self.load()

    def load(self):
        env = 'local'
        if os.path.isfile(self.path):
            with open(self.path) as f:
                env = f.read().strip()

        config_module = __import__('app.config.' + env, fromlist=(env))

        for _c in dir(config_module):
            if _c[0:2] != '__':
                self.config[_c] = getattr(config_module, _c)

    def __getattr__(self, key):
        return self.config.get(key)

    def __str__(self):
        return json.dumps(self.config)
