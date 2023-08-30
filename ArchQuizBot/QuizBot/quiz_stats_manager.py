import pymongo
import config

class QuizStatsManager:
    def __init__(self, db):
        self.db = db

    def record_quiz_attempt(self, user_id, quiz_name, score):
        quiz_stats_collection = self.db["quiz_stats"]
        quiz_stats_collection.update_one({"user_id": user_id, "quiz_name": quiz_name},
                                         {"$set": {"score": score}}, upsert=True)

    def get_user_quiz_scores(self, user_id):
        quiz_stats_collection = self.db["quiz_stats"]
        scores = []
        for quiz_stats in quiz_stats_collection.find({"user_id": user_id}):
            scores.append({"quiz_name": quiz_stats["quiz_name"], "score": quiz_stats["score"]})
        return scores
