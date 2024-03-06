import requests
import html


class Question:

    def __init__(self, text: str, answer: bool):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f"Question: {self.text}, answer: {self.answer}"


class QuestionBank:

    def __init__(self):
        response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
        results = response.json()["results"]
        self.question_bank = [Question(html.unescape(data["question"]), bool(data["correct_answer"])) for data in results]
