import requests


class requests_help(object):
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }

    def __init__(self):
        pass

    def get(self, url, timeout=30):
        body = ''
        try:
            _requests = requests.get(url, timeout=timeout, headers=self._headers)
            body = _requests.text
        except Exception as e:
            print(e)
            pass

        return body

    def setHeader(self, key, value):
        self._headers[key] = value
        return self
