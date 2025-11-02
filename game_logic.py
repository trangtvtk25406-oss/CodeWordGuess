from questions import questions
import random

class GameLogic:
    def __init__(self):
        self.score = 100
        self.current = None
        self.hint_index = 0

    def new_game(self):
        self.current = random.choice(questions)
        self.hint_index = 0
        self.score = 100
        return self.current["hints"][self.hint_index]

    def check_answer(self, user_answer):
        if user_answer.strip().lower() == self.current["answer"].lower():
            return True
        else:
            self.score -= 50
            return False

    def get_hint(self):
        self.hint_index += 1
        if self.hint_index < len(self.current["hints"]):
            return self.current["hints"][self.hint_index]
        return "Hết gợi ý rồi!"