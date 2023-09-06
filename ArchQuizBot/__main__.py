# Broadcast Manager Module - Copyright (c) 2023 itszoney
# This module handles broadcasting messages to subscribed users.
import sys
sys.path.append('/path/to/QuizBot/ArchQuizBot')
from pyrogram import idle
from ArchQuizBot import QuizBot
import config

if __name__ == "__main__":
    quiz_bot = QuizBot()
    quiz_bot.app.run()
