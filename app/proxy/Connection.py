from app.proxy import logger

class Connection(object):
    """TCP server/client connection abstraction."""

    def __init__(self, what):
        self.buffer = b''
        self.closed = False
        self.what = what # server or client
        self.conn = None

    def send(self, data):
        return self.conn.send(data)

    def recv(self, bytes=8192):
        try:
            data = self.conn.recv(bytes)
            if len(data) == 0:
                logger.debug('recvd 0 bytes from %s' % self.what)
                return None
            logger.debug('rcvd %d bytes from %s' % (len(data), self.what))
            return data
        except Exception as e:
            logger.exception('Exception while receiving from connection %s %r with reason %r' % (self.what, self.conn, e))
            return None

    def close(self):
        self.conn.close()
        self.closed = True

    def buffer_size(self):
        return len(self.buffer)

    def has_buffer(self):
        return self.buffer_size() > 0

    def queue(self, data):
        self.buffer += data

    def flush(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]
        logger.debug('flushed %d bytes to %s' % (sent, self.what))
