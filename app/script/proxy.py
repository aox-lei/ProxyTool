# -*- coding:utf-8 -*-
import logging
import argparse
from app.proxy import __version__, __homepage__
from app.proxy.HTTP import HTTP

class proxy(object):
    def run(self):
        parser = argparse.ArgumentParser(
            description='proxy.py v%s' % __version__,
            epilog='Having difficulty using proxy.py? Report at: %s/issues/new' % __homepage__
        )

        parser.add_argument('--hostname', default='127.0.0.1', help='Default: 127.0.0.1')
        parser.add_argument('--port', default='8899', help='Default: 8899')
        parser.add_argument('--log-level', default='INFO', help='DEBUG, INFO, WARNING, ERROR, CRITICAL')
        args = parser.parse_args()

        logging.basicConfig(level=getattr(logging, args.log_level), format='%(asctime)s - %(levelname)s - pid:%(process)d - %(message)s')

        hostname = args.hostname#
        port = int(args.port)

        try:
            proxy = HTTP(hostname, port)
            proxy.run()
        except KeyboardInterrupt:
            pass
