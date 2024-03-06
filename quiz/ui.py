THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import *


# Tkinter in its own class
class QuizInterface:

    def check_true(self):
        self.__check_answer(True)

    def get_next_question(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        if self.quiz_brain.has_more_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz_brain.formatted_next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.disable_buttons()

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

    def check_false(self):
        self.__check_answer(False)

    def __check_answer(self, answer):
        self.disable_buttons()
        if self.quiz_brain.check_answer(answer):
            self.score += 1
        self.give_ui_feedback(answer)

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0;
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 18, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, rowspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, text=quiz_brain.formatted_next_question(),
                                                     width="280", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(highlightthickness=0, image=true_button_image, highlightbackground=THEME_COLOR,
                                  command=self.check_true)
        self.true_button.grid(column=0, row=4)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(highlightthickness=0, image=false_button_image, highlightbackground=THEME_COLOR,
                                   command=self.check_false)
        self.false_button.grid(column=1, row=4)

        self.window.mainloop()

    def give_ui_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.get_next_question)
