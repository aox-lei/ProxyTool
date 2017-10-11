# -*- coding:utf-8 -*-
from app.mongo_model.ip import ip as ipMongo


class base(object):
    def __init__(self):
        pass

    def updateIpInfo(self, ip, is_success=1, speed=0):
        info = ipMongo().info(ip)
        if is_success == 1:
            validate_count = int(info.get('validate_count')) + 1 if int(info.get('validate_count')) < 5 else 5
            ipMongo().updateValidateCount(ip, validate_count, speed)
        else:
            if info is not None and int(info.get('validate_count')) <= -4:
                ipMongo().delete(ip)
            else:
                validate_count = int(info.get('validate_count')) - 1 if int(info.get('validate_count')) > -5 else -5
                ipMongo().updateValidateCount(ip, validate_count, speed)
