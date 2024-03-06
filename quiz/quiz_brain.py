class QuizBrain:

    def __init__(self, questions):
        self.question_number = -1
        self.questions = questions

    def __next_question_with_answer(self):
        self.question_number += 1
        return self.questions[self.question_number]

    def formatted_next_question(self) -> str:
        question = self.__next_question_with_answer()
        return f"{question.text}"

    def has_more_questions(self):
        return self.question_number + 1 <= len(self.questions) - 1

    def check_answer(self, answer : bool) -> bool:
        # print(f"Checking {answer} with answer: {self.questions[self.question_number].answer}")
        answer_answer = self.questions[self.question_number].answer == answer
        # print(f"Result: {answer_answer}")
        return answer_answer

        # else:
        #     print("Sorry, that is incorrect.")
        # print(f"Your score is {self.score} / {len(self.questions)}\n")

        # def print_score(self):
        #     print(f"Your final score was {self.score} / {len(self.questions)}")
