# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     utilFunction.py
   Description :  tool function
   Author :       JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: 添加robustCrawl、verifyProxy、getHtmlTree
-------------------------------------------------
"""
import requests
from lxml import etree

from Util.LogHandler import LogHandler
from Util.WebRequest import WebRequest

logger = LogHandler(__name__)


# noinspection PyPep8Naming
def robustCrawl(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.info(u"sorry, 抓取出错。错误原因:")
            logger.info(e)

    return decorate


# noinspection PyPep8Naming
def verifyProxyFormat(proxy):
    """
    检查代理格式
    :param proxy:
    :return:
    """
    import re
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    return True if re.findall(verify_regex, proxy) else False


# noinspection PyPep8Naming
def getHtmlTree(url, **kwargs):
    """
    获取html树
    :param url:
    :param kwargs:
    :return:
    """

    header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    # TODO 取代理服务器用代理服务器访问
    wr = WebRequest()
    html = wr.get(url=url, header=header).content
    return etree.HTML(html)


# noinspection PyPep8Naming
def validUsefulProxy(proxy):
    """
    检验代理是否可用
    :param proxy:
    :return:
    """
    proxies = {"https": "https://{proxy}".format(proxy=proxy)}
    try:
        # 超过40秒的代理就不要了
        r = requests.get('https://www.baidu.com', proxies=proxies, timeout=40, verify=False)
        if r.status_code == 200:
            logger.debug('%s is ok' % proxy)
            return True
    except Exception as e:
        logger.info(e)
        return False
