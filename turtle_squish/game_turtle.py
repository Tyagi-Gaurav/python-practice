from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reset_position()

    def move_up(self):
        self.forward(10)

    def reset_position(self):
        self.setheading(90)
        self.goto(10, -270)

    def has_reached_top(self):
        return self.ycor() >= 290
