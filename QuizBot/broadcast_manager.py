# Broadcast Manager Module - Copyright (c) 2023 itszoney
# This module handles broadcasting messages to subscribed users.

import pymongo
import config

class BroadcastManager:
    def __init__(self, db):
        self.db = db

    def send_broadcast_to_chats(self, text):
        for chat_data in self.db[config.MONGO_CHATS_COLLECTION].find():
            chat_id = chat_data["_id"]
            try:
                self.app.send_message(chat_id, text)
            except Exception as e:
                print(f"Failed to send broadcast to chat {chat_id}: {e}")
