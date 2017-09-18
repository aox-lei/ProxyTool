import time
import math
from app.validate.base import base
from app.util.requests_help import requests_help
from app.util.log import log


class request_web(base):
    _url = 'http://www.qq.com'

    def run(self, http_type, ip, port):
        _request_handle = requests_help()
        _result = _request_handle.setProxy(http_type, ip, port).setHeader('current_time', str(time.time())).get(self._url, 10)

        if len(_result) > 0:
            speed = math.ceil(time.time() - float(_request_handle.getRequestHeader('current_time')))
            self.updateIpInfo(ip, is_success=1, speed=speed)
            log().info(ip + ' 验证通过')
        else:
            self.updateIpInfo(ip, is_success=0)
            log().info(ip + ' 验证失败')
