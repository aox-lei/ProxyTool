# -*- coding:utf-8 -*-
import sys
from bs4 import BeautifulSoup
from app.crawl.base import base
from app.util.function import now


class ip181(base):
    max_page = 5
    index_url = 'http://www.ip181.com/'
    list_url = 'http://www.ip181.com/daili/%d.html'

    def run(self):
        self._crawl_single(self.index_url)
        self._crawl_page(self.list_url)

    def _parse_html(self, html):
        soup = BeautifulSoup(html, 'lxml')
        _ip_html = soup.select('table.ctable > tbody > tr > td:nth-of-type(1)')
        del _ip_html[0]

        _port_html = soup.select('table.ctable > tbody > tr > td:nth-of-type(2)')
        del _port_html[0]
        _is_anonymous_html = soup.select('table.ctable > tbody > tr > td:nth-of-type(3)')
        del _is_anonymous_html[0]
        _type_html = soup.select('table.ctable > tbody > tr > td:nth-of-type(4)')
        del _type_html[0]

        data = []
        for index, value in enumerate(_ip_html):
            _data = {
                'country': 'cn',
                'ip': _ip_html[index].text.strip(),
                'port': _port_html[index].text.strip(),
                'type': 'ALL' if _type_html[index].text.strip() == 'HTTP,HTTPS' else _type_html[index].text.strip(),
                'is_anonymous': 0 if _is_anonymous_html[index].text.strip() == '透明' else 1,
                'is_validate': 0,
                'validate_count': 0,
                'create_time': now(),
                'validate_time': now()
            }
            data.append(_data)
        return data
