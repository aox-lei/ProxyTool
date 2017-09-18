import requests
from app.util.log import log


class requests_help(object):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }
    _proxy = {}
    _meta = {}

    def __init__(self):
        pass

    def get(self, url, timeout=30):
        body = ''
        try:
            _result = requests.get(url, timeout=timeout, headers=self._headers, proxies=self._proxy)
            body = _result.text
            self._request = _result.request
        except Exception as e:
            log().warning('请求失败' + e)

        return body

    def setHeader(self, key, value):
        self._headers[key] = value
        return self

    def setProxy(self, http_type, ip, port):
        self._proxy = {
            http_type: '%s://%s:%s' % (http_type, ip, port)
        }

        return self

    def getRequestHeader(self, key):
        if hasattr(self, '_request'):
            return self._request.headers.get(key)
        else:
            return None
