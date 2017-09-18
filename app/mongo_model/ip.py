# -*- coding:utf-8 -*-
from pymongo import ASCENDING, DESCENDING
from app.mongo_model.base import base
from app.mongo_model import db
from app.util.function import now
from app.util.log import log


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
        except Exception as e:
            log().warning('添加数据失败:' + e)

    def addMany(self, data):
        '''
            批量添加代理ip
        '''
        try:
            self.collection.insert_many(data)
        except Exception as e:
            log().warning('批量添加数据失败:' + e)

    def listByIp(self, ip_list):
        ''' 根据ip查询是否存在 '''
        data = []
        try:
            cursor = self.collection.find({'ip': {'$in': ip_list}}, {'ip': 1})
            data = [_cursor.get('ip') for _cursor in cursor]
        except Exception as e:
            log().warning('根据ipList查询数据失败:' + e)

        return data

    def lists(self, limit):
        ''' 查询指定数量的ip '''
        data = []
        try:
            cursor = self.collection.find().sort('validate_time', ASCENDING).limit(limit)
            data = [_cursor for _cursor in cursor]
        except Exception as e:
            log().warning('查看数据失败:' + e)
        return data

    def listsValid(self, limit):
        ''' 有效代理 '''
        data = []
        _where = {'is_validate': 1,
                  'validate_count': {'$gt': 0},
                  'speed': {'$gt': 0}}
        _field = {'type': 1, 'ip': 1, 'port': 1, '_id': 0, 'speed': 1}
        try:
            cursor = self.collection.find(_where, _field).sort('validate_time', DESCENDING).sort('speed', ASCENDING).limit(limit)
            data = [_cursor for _cursor in cursor]
        except Exception as e:
            log().warning('查看数据失败:' + e)
        return data

    def info(self, ip):
        ''' 获取ip的信息'''
        info = {}
        try:
            info = self.collection.find_one({'ip': ip}, {'ip': 1, 'port': 1, 'type': 1, 'is_anonymous': 1, 'validate_count': 1})
        except Exception as e:
            log().warning('查看数据失败:' + e)
        return info

    def updateValidateCount(self, ip, validate_count, speed=0):
        ''' 更新ip验证信息'''
        try:
            result = self.collection.update({'ip': ip}, {
                '$set': {
                    'is_validate': 1,
                    'validate_count': validate_count,
                    'speed': speed,
                    'validate_time': now()
                }})
        except Exception as e:
            log().warning('更新数据失败:' + e)

        return result

    def delete(self, ip):
        ''' 删除指定ip的数据 '''
        try:
            result = self.collection.delete_one({'ip': ip})
        except Exception as e:
            log().warning('更新数据失败:' + e)

        return result
