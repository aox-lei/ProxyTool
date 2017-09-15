from app.mongo_model.ip import ip
from app.validate.requst_web import request_web


class validate(object):
    def run(self):
        _lists = ip().lists(100)

        for _i in _lists:
            pass
