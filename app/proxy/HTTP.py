# -*- coding:utf-8 -*-
from app.proxy.TCP import TCP
from app.proxy.Proxy import Proxy
from app.proxy import logger

class HTTP(TCP):
    """HTTP proxy server implementation.

    Spawns new process to proxy accepted client connection.
    """

    def handle(self, client):
        proc = Proxy(client)
        proc.daemon = True
        proc.start()
        logger.debug('Started process %r to handle connection %r' % (proc, client.conn))
