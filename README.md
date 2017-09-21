# ProxyTool
python3搭建的代理池功能, 免费获取代理ip 每10分钟自动抓取ip66、ip181、xici代理的脚本, 保存到mongo中, 并且提供web接口, 方便搭建调用
环境: python3.6.2
## 一、安装方法
```
pip install -r requirements.txt
```

## 二、使用方法
-env 指定环境, 会读取app.config下指定的配置文件
```
python run.py -env online
```

## 三、 基本逻辑
整个项目分为三部分 抓取、验证和web接口
### 一、抓取
在app/crawl目录下, 每个网站对应的一个文件, 可以自己扩展, 基本代码可以查看app/crawl/下的文件
```
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
        要抓取的url可以传入, 抓取列表页调用self._crawl_page, 抓取单页调用_crawl_single

    def _parse_html(self, html):
        抓取后, 将页面中的内容解析出来
```

### 二、验证
验证是在app/validate目录下, 目前只实现了请求百度验证的方式

### 三、web接口
web接口目前只实现的get接口, 默认绑定端口为8899
访问地址:http://网址/get/<要获取的ip数量>
```
[
    {
        ip: "114.82.159.57",
        type: "HTTPS", # type有三个值, https,http和all, all代表支持http和https两种
        port: "8118",
        speed: 1 # 请求速度, 越小说明越快
    },
    {
        ip: "223.150.73.245",
        type: "HTTP",
        port: "80",
        speed: 1
    }
]
```

如果在使用中有什么问题可以发issue, 如果真的对您有什么作用的话, 请给个star
