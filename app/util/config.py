import json


class config(object):
    _env = []
    _config = {}

    def __init__(self, env='local'):
        if len(self._env) == 0:
            self._env.append(env)

        if len(self._config) == 0:
            self._load()

    def _load(self):
        config_module = __import__('app.config.' + self._env[0], fromlist=(self._env[0]))

        for _c in dir(config_module):
            if _c[0:2] != '__':
                self._config[_c] = getattr(config_module, _c)

    def __getattr__(self, key):
        return self._config.get(key)

    def __str__(self):
        return json.dumps(self._config)
