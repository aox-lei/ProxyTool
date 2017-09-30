# -*- coding:utf-8 -*-
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from app.util.config import config


class crawl(object):
    def run(self):
        self._run()
        scheduler = BlockingScheduler()
        scheduler.add_job(self._run, 'interval', minutes=10)
        scheduler.start()

    def _run(self):
        web_site = config().crawl_web_site
        _thread = []
        for _site in web_site:
            _module = __import__('app.crawl.' + _site, fromlist=(_site))
            _class = getattr(_module, _site)
            _thread.append(threading.Thread(target=_class().run))

        for _p in _thread:
            _p.start()
