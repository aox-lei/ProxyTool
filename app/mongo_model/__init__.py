from pymongo import MongoClient
from app.util.config import config

client = MongoClient(config().mongo_dsn)
db = client[config().db]
