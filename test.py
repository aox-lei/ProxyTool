from app.util.config import config

config().load()

print(config().mongo_dsn)
