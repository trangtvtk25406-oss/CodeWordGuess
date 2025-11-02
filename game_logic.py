from questions import questions
import random

# Các biến để lưu trạng thái
score = 100
current = None
hint_index = 0

    def new_game(self):
        """Bắt đầu trò chơi mới và trả về gợi ý đầu tiên"""
        global current, hint_index, score
        current = random.choice(questions)
        hint_index = 0
        score = 100
        return current["hints"][hint_index]
    
    def check_answer(user_answer):
        """Kiểm tra đáp án người chơi"""
        global score
        if current and user_answer.strip().lower() == current["answer"].lower():
            return True
        else:
            score -= 50
            return False

    def get_hint():
        """Trả về gợi ý tiếp theo nếu còn"""
        global hint_index
        hint_index += 1
        if current and hint_index < len(current["hints"]):
            return current["hints"][hint_index]
        return "Hết gợi ý rồi!"


