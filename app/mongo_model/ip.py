from pymongo import ASCENDING
from app.mongo_model.base import base
from app.mongo_model import db


class ip(base):
    __collection__ = 'ip'

    def __init__(self):
        self.collection = db[self.__collection__]

    def add(self, data):
        '''
            添加一个ip
            :param data dict{ ip数据
                country: 国家
                ip: ip地址
                port: 端口
                type: 类型 (http/https)
                is_anonymous: 是否高匿 1是 0:不是
            }
        '''
        try:
            self.collection.insert_one(data)
        except:
            pass

    def addMany(self, data):
        '''
            批量添加代理ip
        '''
        self.collection.insert_many(data)

    def listByIp(self, ip_list):
        ''' 根据ip查询是否存在 '''
        cursor = self.collection.find({'ip': {'$in': ip_list}}, {'ip': 1})
        data = [_cursor.get('ip') for _cursor in cursor]

        return data

    def lists(self, limit):
        cursor = self.collection.find().sort('validate_time', ASCENDING).limit(limit)
        data = [_cursor for _cursor in cursor]
        return data
