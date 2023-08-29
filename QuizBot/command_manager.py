class CommandManager:
    def __init__(self, app, user_manager, chat_manager, quiz_manager, broadcast_manager, logger_manager):
        self.app = app
        self.user_manager = user_manager
        self.chat_manager = chat_manager
        self.quiz_manager = quiz_manager
        self.broadcast_manager = broadcast_manager
        self.logger_manager = logger_manager

    def handle_start_command(self, message):
        user_id = message.from_user.id
        self.user_manager.initialize_user(user_id)

        start_button = InlineKeyboardButton("Start Quiz", callback_data="start_quiz")
        inline_keyboard = InlineKeyboardMarkup([[start_button]])

        message.reply_text("Welcome to the quiz bot! Press the button below to start the quiz.",
                           reply_markup=inline_keyboard)

    def handle_broadcast_command(self, message):
        user_id = message.from_user.id
        is_subscribed = self.user_manager.toggle_broadcast_subscription(user_id)

        if is_subscribed:
            message.reply_text("You are now subscribed to broadcasts.")
        else:
            message.reply_text("You are now unsubscribed from broadcasts.")

#copyrigts by telegram @itszoney
    def handle_callback_start_quiz(self, query):
        user_id = query.from_user.id
        self.quiz_manager.start_quiz(user_id, "quiz_name")

        query.answer("Starting the quiz!")


    def handle_forward_logs(self, message):
        if message.from_user.id == config.BOT_OWNER_ID:
            self.logger_manager.forward_logs_to_owner(message)

    def handle_chat_member_updated(self, update, context):
        if update.new_chat_member:
            self.logger_manager.log_join_event(update)
        elif update.left_chat_member:
            self.logger_manager.log_leave_event(update)
