from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.__update_score_board()

    def update(self):
        self.level += 1
        self.__update_score_board()

    def __update_score_board(self):
        self.clear()
        self.goto(-340, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 250)
        self.write(f"Game Over!", align="center", font=("Courier", 20, "normal"))
