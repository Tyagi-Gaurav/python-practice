import data
from quiz_brain import QuizBrain


class Question:

    def __init__(self, text, answer):
        self.answer = answer
        self.text = text

    def __str__(self):
        return f"Question: {self.text}, answer: {self.answer}"


question_bank = []

for question in data.question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_more_questions():
    q_number, question = quiz_brain.next_question()
    answer = input(f"{q_number}. {question}? (True/False): ")
    quiz_brain.check_answer(q_number, answer)

print ("You have completed the quiz.")
quiz_brain.print_score()
