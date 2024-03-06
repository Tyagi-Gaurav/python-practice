from question_model import *
from ui import *

question_model = QuestionBank()
quiz_brain = QuizBrain(question_model.question_bank)
quizInterface = QuizInterface(quiz_brain)
