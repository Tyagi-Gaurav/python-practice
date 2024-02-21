from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.__update_score_board()

    def update_left(self):
        self.l_score += 1
        self.__update_score_board()

    def __update_score_board(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_right(self):
        self.r_score += 1
        self.__update_score_board()
