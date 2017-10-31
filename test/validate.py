# -*- coding:utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from app.validate.request_web import request_web

request_web().run('http', '222.73.68.144', 8090)
