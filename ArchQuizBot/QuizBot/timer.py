import time

class TimerManager:
    def __init__(self):
        self.question_start_time = None

    def start_question_timer(self):
        self.question_start_time = time.time()

    def get_elapsed_time(self):
        if self.question_start_time:
            return time.time() - self.question_start_time
        return 0
