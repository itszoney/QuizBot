import pymongo
import config

class DatabaseManager:
    def __init__(self):
        self.db_client = pymongo.MongoClient(config.MONGO_URI)
        self.db = self.db_client[config.MONGO_DB_NAME]

    def get_users_collection(self):
        return self.db[config.MONGO_USERS_COLLECTION]

    def get_chats_collection(self):
        return self.db[config.MONGO_CHATS_COLLECTION]

