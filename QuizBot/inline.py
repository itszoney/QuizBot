from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram #import InlineQueryResultArticle, InputTextMessageContent

class InlineManager:
    def __init__(self, app, formatter, quiz_manager):
        self.app = app
        self.formatter = formatter
        self.quiz_manager = quiz_manager

    def handle_inline_query(self, query):
        user_id = query.from_user.id
        quiz_name = "quiz_name"  # Replace with the actual quiz name

        quiz_questions = self.quiz_manager.get_quiz_questions(quiz_name)
        results = []

        for question in quiz_questions:
            formatted_question = self.formatter.format_quiz_question(question["question"], question["options"])
            result = InlineQueryResultArticle(id=question["_id"], title="Quiz Question",
                                              input_message_content=InputTextMessageContent(formatted_question))
            results.append(result)

        self.app.answer_inline_query(query.id, results)
