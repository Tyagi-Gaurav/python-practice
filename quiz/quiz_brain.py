class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def next_question(self):
        self.question_number += 1
        return self.question_number, self.questions[self.question_number]

    def has_more_questions(self):
        return self.question_number + 1 <= len(self.questions) - 1

    def check_answer(self, number, answer):
        if self.questions[number].answer == answer:
            self.score += 1
            print(f"You are correct!.")
        else:
            print("Sorry, that is incorrect.")
        print(f"Your score is {self.score} / {len(self.questions)}\n")

    def print_score(self):
        print(f"Your final score was {self.score} / {len(self.questions)}")
