import pymongo
import config

class UserManager:
    def __init__(self, db):
        self.db = db

    def initialize_user(self, user_id):
        users_collection = self.db[config.MONGO_USERS_COLLECTION]
        users_collection.update_one({"_id": user_id}, {"$setOnInsert": {"broadcast_subscribed": False}}, upsert=True)

    def toggle_broadcast_subscription(self, user_id):
        users_collection = self.db[config.MONGO_USERS_COLLECTION]
        user_data = users_collection.find_one({"_id": user_id})
        
        if user_data:
            current_subscribed = user_data.get("broadcast_subscribed", False)
            users_collection.update_one({"_id": user_id}, {"$set": {"broadcast_subscribed": not current_subscribed}})
            return not current_subscribed

    def get_broadcast_subscribers(self):
        subscribers = []
        for user_data in self.db[config.MONGO_USERS_COLLECTION].find({"broadcast_subscribed": True}):
            subscribers.append(user_data["_id"])
        return subscribers

#copyrigts by telegram @itszoney