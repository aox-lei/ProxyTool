import threading
import time
from app.mongo_model.ip import ip
from app.validate.requst_web import request_web


class validate(object):
    def run(self):
        while(True):
            _lists = ip().lists(100)

            _threads = []
            for _i in _lists:
                _http_type = 'http' if _i.get('type') == 'ALL' else _i.get('type')
                _t = threading.Thread(target=request_web().run, args=(_http_type, _i.get('ip'), _i.get('port')))
                _threads.append(_t)

            for t in _threads:
                t.start()

            for t in _threads:
                t.join()

            time.sleep(10)
