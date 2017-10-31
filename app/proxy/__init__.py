import logging
VERSION = (0, 2)
__version__ = '.'.join(map(str, VERSION[0:2]))
__description__ = 'HTTP Proxy Server in Python'
__author__ = 'Abhinav Singh'
__author_email__ = 'mailsforabhinav@gmail.com'
__homepage__ = 'https://github.com/abhinavsingh/proxy.py'
__license__ = 'BSD'

CRLF, COLON, SP = b'\r\n', b':', b' '

HTTP_REQUEST_PARSER = 1
HTTP_RESPONSE_PARSER = 2

HTTP_PARSER_STATE_INITIALIZED = 1
HTTP_PARSER_STATE_LINE_RCVD = 2
HTTP_PARSER_STATE_RCVING_HEADERS = 3
HTTP_PARSER_STATE_HEADERS_COMPLETE = 4
HTTP_PARSER_STATE_RCVING_BODY = 5
HTTP_PARSER_STATE_COMPLETE = 6

CHUNK_PARSER_STATE_WAITING_FOR_SIZE = 1
CHUNK_PARSER_STATE_WAITING_FOR_DATA = 2
CHUNK_PARSER_STATE_COMPLETE = 3

text_type = str
binary_type = bytes


def text_(s, encoding='utf-8', errors='strict'):
    """ If ``s`` is an instance of ``binary_type``, return
    ``s.decode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, binary_type):
        return s.decode(encoding, errors)
    return s  # pragma: no cover


def bytes_(s, encoding='utf-8', errors='strict'):
    """ If ``s`` is an instance of ``text_type``, return
    ``s.encode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, text_type):  # pragma: no cover
        return s.encode(encoding, errors)
    return s

logger = logging.getLogger(__name__)
version = bytes_(__version__)
