# -*- coding:utf-8 -*-
import os
import sys

sys.path.append(os.path.abspath(os.getcwd()))

from app.script.proxy import proxy

proxy().run()
