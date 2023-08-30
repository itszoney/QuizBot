import pymongo
import config

class QuizManager:
    def __init__(self, db):
        self.db = db

    def start_quiz(self, user_id, quiz_name):
        # Your implementation to start a quiz for a user
        pass

    def get_quiz_questions(self, quiz_name):
        # Your implementation to retrieve quiz questions
        pass

    def submit_quiz_answer(self, user_id, question_id, answer):
        # Your implementation to submit a user's answer for a question
        pass

    def get_user_score(self, user_id, quiz_name):
        # Your implementation to get a user's score for a specific quiz
        pass
