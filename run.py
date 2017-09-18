from multiprocessing import Process
from apscheduler.schedulers.blocking import BlockingScheduler
from app.script.crawl import crawl
from app.script.validate import validate
from app.script import web

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(crawl().run, 'interval', minutes=1)
    scheduler.start()
    _process = []
    _process.append(Process(target=validate().run))
    _process.append(Process(target=web.run))

    for _p in _process:
        _p.start()
