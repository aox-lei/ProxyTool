# -*- coding:utf-8 -*-
import json
from flask import Flask
from app.mongo_model.ip import ip
from app.util.config import config

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/get/<int:num>')
def get(num):
    lists = ip().listsValid(num)
    return json.dumps(lists)


def run():
    if config().debug == 1:
        app.run(host='0.0.0.0', port=8899, debug=True)
    else:
        app.run(host='0.0.0.0', port=8899)
