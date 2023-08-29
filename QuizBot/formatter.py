class Formatter:
    @staticmethod
    def format_quiz_question(question, options):
        formatted_question = f"Q: {question}\n\n"
        for i, option in enumerate(options, start=1):
            formatted_question += f"{i}. {option}\n"
        return formatted_question
