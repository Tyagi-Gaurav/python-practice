from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align="center", font=('Arial', 16, 'normal'))
