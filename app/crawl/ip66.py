from bs4 import BeautifulSoup
from app.crawl.base import base
from app.util.function import now


class ip66(base):
    max_page = 5
    list_url = 'http://www.66ip.cn/%d.html'

    def run(self):
        self._crawl_page(self.list_url)

    def _parse_html(self, html):
        ''' 从内容中解析ip'''
        soup = BeautifulSoup(html, 'lxml')
        _ip_html = soup.select('#main > div > div:nth-of-type(1) > table > tr > td:nth-of-type(1)')
        del _ip_html[0]
        _port_html = soup.select('#main > div > div:nth-of-type(1) > table > tr > td:nth-of-type(2)')
        del _port_html[0]
        _is_anonymous_html = soup.select('#main > div > div:nth-of-type(1) > table > tr > td:nth-of-type(4)')
        del _is_anonymous_html[0]

        data = []
        for index, value in enumerate(_ip_html):
            _data = {
                'country': 'cn',
                'ip': _ip_html[index].text.strip(),
                'port': _port_html[index].text.strip(),
                'type': 'HTTP',
                'is_anonymous': 1 if _is_anonymous_html[index].text.strip() == '高匿代理' else 0,
                'is_validate': 0,
                'validate_count': 0,
                'source': 'ip66',
                'create_time': now(),
                'validate_time': now()
            }
            data.append(_data)
        return data
