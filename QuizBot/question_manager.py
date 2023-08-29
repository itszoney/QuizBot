import pymongo
import config

class QuestionManager:
    def __init__(self, db):
        self.db = db

    def create_question(self, question, options, correct_answer):
        questions_collection = self.db["quiz_questions"]
        questions_collection.insert_one({
            "question": question,
            "options": options,
            "correct_answer": correct_answer
        })

    def get_question(self, question_id):
        questions_collection = self.db["quiz_questions"]
        return questions_collection.find_one({"_id": question_id})
