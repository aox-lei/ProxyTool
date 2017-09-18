import time
from app.mongo_model.ip import ip
from app.util.requests_help import requests_help


class base(object):
    def __init__(self):
        pass

    def _save(self, data):
        ''' 保存数据到mongo '''
        ip_list = [value.get('ip')for index, value in enumerate(data)]
        ip_list = ip().listByIp(ip_list)

        if len(ip_list) > 0:
            data = [_data for _index, _data in enumerate(data) if _data.get('ip') not in ip_list]

        if len(data) > 0:
            ip().addMany(data)

    def _crawl_single(self, url):
        ''' 抓取单个页面'''
        _body = requests_help().get(url)
        if _body:
            _data = self._parse_html(_body)

        self._save(_data)

    def _crawl_page(self, url):
        ''' 分页抓取 '''
        for i in range(0, self.max_page):
            _url = url % (int(i) + 1)
            self._crawl_single(_url)
            time.sleep(5)
