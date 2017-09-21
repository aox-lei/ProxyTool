# -*- coding:utf-8 -*-
import argparse

from multiprocessing import Process
from app.script.crawl import crawl
from app.script.validate import validate
from app.script import web
from app.util.init import init


parse = argparse.ArgumentParser()
parse.add_argument('-env', help="设置环境", type=str)
args = parse.parse_args()

env = args.env if args.env is not None else 'local'
init(env)


if __name__ == '__main__':
    _process = []
    _process.append(Process(target=crawl().run))
    _process.append(Process(target=validate().run))
    _process.append(Process(target=web.run))

    for _p in _process:
        _p.start()
