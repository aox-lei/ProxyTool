# -*- coding:utf-8 -*-
import requests


class requests_help(object):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }
    _proxy = {}
    _meta = {}
    _request = None

    def __init__(self):
        pass

    def get(self, url, timeout=30):
        body = ''
        try:
            _result = requests.get(url, timeout=timeout, headers=self._headers, proxies=self._proxy)
            body = _result.text
            self._request = _result.request

            return body
        except:
            return False

    def setHeader(self, key, value):
        self._headers[key] = value
        return self

    def setProxy(self, req_http_type, http_type, ip, port):
        self._proxy = {
            req_http_type: '%s://%s:%s' % (http_type, ip, port),
        }

        return self

    def getRequestHeader(self, key):
        if self._request is not None:
            try:
                return self._request.headers.get(key)
            except:
                return None
        else:
            return None
