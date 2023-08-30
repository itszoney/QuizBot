import config

class LoggerManager:
    def __init__(self, app):
        self.app = app

    def forward_logs_to_owner(self, message):
        self.app.forward_messages(config.BOT_OWNER_ID, message.chat.id, message.message_id)

    def log_join_event(self, update):
        chat_id = update.chat.id
        user_id = update.from_user.id
        user_first_name = update.from_user.first_name

        self.app.send_message(config.LOGGER_GROUP_ID, f"{user_first_name} joined the chat (ID: {user_id})")

    def log_leave_event(self, update):
        chat_id = update.chat.id
        user_id = update.from_user.id
        user_first_name = update.from_user.first_name

        self.app.send_message(config.LOGGER_GROUP_ID, f"{user_first_name} left the chat (ID: {user_id})")
