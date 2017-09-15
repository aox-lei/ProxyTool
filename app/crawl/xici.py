import sys
from bs4 import BeautifulSoup
from app.util.requests_help import requests_help
from app.crawl.base import base


class xici(base):
    max_page = 10
    anonymous_proxy_url = 'http://www.xicidaili.com/nn/%d'
    common_proxy_url = 'http://www.xicidaili.com/nt/%d'
    https_proxy_url = 'http://www.xicidaili.com/wn/%d'
    http_proxy_url = 'http://www.xicidaili.com/wt/%d'

    def run(self):
        _anonymous_list = self.crawl_anonymous()
        pass

    def crawl_anonymous(self):
        '''
            抓取高匿代理ip
        '''
        for i in range(1, self.max_page):
            _url = self.anonymous_proxy_url % (i)
            _body = requests_help().get(_url)
            _list = self.parse_html(_body)
            sys.exit()

    def parse_html(self, body):
        ''' 从内容中解析ip'''
        soup = BeautifulSoup(body, 'lxml')
        _country_html = soup.select('#ip_list > tr > td.country > img')
        _ip_html = soup.select('#ip_list > tr > td:nth-of-type(2)')
        _country = []
        _ip = []
        for index, value in enumerate(_country_html):
            _country.insert(index, value.attrs.get('alt'))
            _ip.insert(index, _ip_html[index].text)
            print(_ip)
            sys.exit()
        pass
