from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=0.5)
        self.shape("square")
        self.goto(initial_x, initial_y)

    def move_up(self):
        if self.ycor() + 20 <= 350:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() - 20 > -350:
            self.goto(self.xcor(), self.ycor() - 20)
