from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pymongo
import config

class QuizBot:
    def __init__(self):
        self.app = Client("quiz_bot", config.API_ID, config.API_HASH, bot_token=config.BOT_TOKEN)
        self.bot_owner_id = config.BOT_OWNER_ID
        self.logger_group_id = config.LOGGER_GROUP_ID
        self.db_client = pymongo.MongoClient(config.MONGO_URI)
        self.db = self.db_client[config.MONGO_DB_NAME]

        @self.app.on_message(filters.command("start"))
        def start(self, message: Message):
            user_id = message.from_user.id
            self.user_manager.initialize_user(user_id)

            start_button = InlineKeyboardButton("Start Quiz", callback_data="start_quiz")
            inline_keyboard = InlineKeyboardMarkup([[start_button]])

            message.reply_text("Welcome to the quiz bot! Press the button below to start the quiz.",
                               reply_markup=inline_keyboard)

        @self.app.on_callback_query(filters.callback_data("start_quiz"))
        def callback_start_quiz(self, query):
            user_id = query.from_user.id
            self.user_manager.start_quiz(user_id, "quiz_name")

            query.answer("Starting the quiz!")

        @self.app.on_message(filters.private & filters.user(self.bot_owner_id))
        def forward_logs_to_owner(self, message: Message):
            self.app.forward_messages(self.bot_owner_id, message.chat.id, message.message_id)

        @self.app.on_chat_member_updated()
        def log_join_leave(self, update, context):
            chat_id = update.chat.id
            user_id = update.from_user.id
            user_first_name = update.from_user.first_name

            if update.new_chat_member:
                self.app.send_message(self.logger_group_id, f"{user_first_name} joined the chat (ID: {user_id})")
            elif update.left_chat_member:
                self.app.send_message(self.logger_group_id, f"{user_first_name} left the chat (ID: {user_id})")

    def run(self):
        self.app.run()

if __name__ == "__main__":
    bot = QuizBot()
    bot.run()
#copyrigts by telegram @itszoney