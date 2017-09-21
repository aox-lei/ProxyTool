from multiprocessing import Process
from apscheduler.schedulers.blocking import BlockingScheduler
from app.util.config import config


class crawl(object):
    def run(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self._run, 'interval', minutes=10)
        scheduler.start()

    def _run(self):
        web_site = config().crawl_web_site
        _process = []
        for _site in web_site:
            _module = __import__('app.crawl.' + _site, fromlist=(_site))
            _class = getattr(_module, _site)
            _process.append(Process(target=_class().run))

        for _p in _process:
            _p.start()
            _p.join()
