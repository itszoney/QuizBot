import pymongo
import config

class ChatManager:
    def __init__(self, db):
        self.db = db

    def save_chat_data(self, chat_id, data):
        chats_collection = self.db[config.MONGO_CHATS_COLLECTION]
        chats_collection.update_one({"_id": chat_id}, {"$set": data}, upsert=True)

    def get_chat_data(self, chat_id):
        chats_collection = self.db[config.MONGO_CHATS_COLLECTION]
        return chats_collection.find_one({"_id": chat_id})

    def get_all_chats(self):
        chat_list = []
        for chat_data in self.db[config.MONGO_CHATS_COLLECTION].find():
            chat_list.append(chat_data)
        return chat_list
#copyrigts by telegram @itszoney