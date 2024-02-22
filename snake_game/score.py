from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.read_high_score()
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center", font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_score()
        self.update_high_score()

    def read_high_score(self):
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents)

    def update_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
