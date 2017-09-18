import json
from flask import Flask
from app.mongo_model.ip import ip

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/get/<int:num>')
def get(num):
    lists = ip().listsValid(num)
    print(lists)
    return json.dumps(lists)


def run():
    app.run(host='0.0.0.0', port=8899, debug=True)
