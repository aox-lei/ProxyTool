from bs4 import BeautifulSoup
from app.util.function import now
from app.crawl.base import base


class xici(base):
    # 最大抓取页数
    max_page = 3
    anonymous_proxy_url = 'http://www.xicidaili.com/nn/%d'
    common_proxy_url = 'http://www.xicidaili.com/nt/%d'
    https_proxy_url = 'http://www.xicidaili.com/wn/%d'
    http_proxy_url = 'http://www.xicidaili.com/wt/%d'

    def run(self):
        self._crawl_page(self.anonymous_proxy_url)
        self._crawl_page(self.common_proxy_url)
        self._crawl_page(self.https_proxy_url)
        self._crawl_page(self.http_proxy_url)

    def _parse_html(self, html):
        ''' 从内容中解析ip'''
        soup = BeautifulSoup(html, 'lxml')
        _ip_html = soup.select('#ip_list > tr > td:nth-of-type(2)')
        _port_html = soup.select('#ip_list > tr > td:nth-of-type(3)')
        _type_html = soup.select('#ip_list > tr > td:nth-of-type(6)')
        _is_anonymous_html = soup.select('#ip_list > tr > td:nth-of-type(5)')

        data = []
        for index, value in enumerate(_ip_html):
            _data = {
                'country': 'cn',
                'ip': _ip_html[index].text.strip(),
                'port': _port_html[index].text.strip(),
                'type': _type_html[index].text.strip(),
                'is_anonymous': 1 if _is_anonymous_html[index].text.strip() == '高匿' else 0,
                'is_validate': 0,
                'validate_count': 0,
                'source': 'xicidaili',
                'create_time': now(),
                'validate_time': now()
            }
            data.append(_data)
        return data
