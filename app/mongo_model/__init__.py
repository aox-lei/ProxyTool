from pymongo import MongoClient
from app.util.config import config

client = MongoClient(config().mongo_dsn, connect=False)
db = client[config().mongo_db]
