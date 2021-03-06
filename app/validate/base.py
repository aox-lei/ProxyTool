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
            validate_count = 0 if info is None or 'validate_count' not in info else int(info.get('validate_count'))

            if validate_count <= -4:
                ipMongo().delete(ip)
            else:
                validate_count = validate_count - 1 if validate_count > -5 else -5
                ipMongo().updateValidateCount(ip, validate_count, speed)
