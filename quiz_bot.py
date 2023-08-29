# Broadcast Manager Module - Copyright (c) 2023 itszoney
# This module handles broadcasting messages to subscribed users.
#from QuizBot.quiz_bot import QuizBot
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent
import config
from QuizBot import user_manager
from QuizBot import chat_manager
from QuizBot import broadcast_manager
from QuizBot import quiz_manager
from QuizBot import logger_manager
from QuizBot import quiz_stats_manager
from QuizBot import command_manager
from QuizBot import inline_manager
from QuizBot import timer_manager
from QuizBot import question_manager
from QuizBot import utils
from QuizBot import database
from QuizBot import formatter

app = Client(
    config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

db_manager = database.DatabaseManager()
user_manager = user_manager.UserManager(db_manager)
chat_manager = chat_manager.ChatManager(db_manager)
broadcast_manager = broadcast_manager.BroadcastManager(db_manager)
quiz_manager = quiz_manager.QuizManager(db_manager)
logger_manager = logger_manager.LoggerManager(app)
quiz_stats_manager = quiz_stats_manager.QuizStatsManager(db_manager)
formatter = formatter.Formatter()
utils = utils.Utils()
timer_manager = timer_manager.TimerManager()
question_manager = question_manager.QuestionManager(db_manager)
inline_manager = inline_manager.InlineManager(app, formatter, quiz_manager)

command_manager = command_manager.CommandManager(
    app, user_manager, chat_manager, quiz_manager, broadcast_manager,
    logger_manager, inline_manager, timer_manager, question_manager, quiz_stats_manager
)

@app.on_message(filters.private | filters.group)
def handle_message(client, message):
    command_manager.handle_forward_logs(message)
    if message.text and message.text.startswith("/start"):
        command_manager.handle_start_command(message)
    # Add more message handling logic as needed

@app.on_callback_query()
def handle_callback_query(client, query):
    command_manager.handle_callback_query(query)

@app.on_inline_query()
def handle_inline_query(client, query):
    inline_manager.handle_inline_query(query)

@app.on_chat_member_updated()
def handle_chat_member_updated(client, update, context):
    command_manager.handle_chat_member_updated(update, context)

if __name__ == "__main__":
    app.run()
