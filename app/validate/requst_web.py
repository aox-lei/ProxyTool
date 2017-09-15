from app.validate.base import base

from app.util.requests_help import requests_help


class request_web(base):
    _url = 'https://www.baidu.com'

    def run(self):
        _result = requests_help.get(self._url, 10)

        if len(_result) > 0:
            return True
        else:
            return False
