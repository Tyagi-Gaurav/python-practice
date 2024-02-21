from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.setheading(100)
        self.penup()
        self.increment = 20

    def move(self):
        self.forward(self.increment)
        if self.ycor() >= 370:  # Hitting the top wall
            self.setheading(180 - self.heading())
            self.increment = -20
        elif self.ycor() <= -370:  # Hitting the bottom wall
            self.setheading(180 - self.__to_quadrant_angle())
            self.increment = 20

    def __to_quadrant_angle(self):
        angle = self.heading()
        if 180 < angle < 270:
            return 270 - angle
        elif angle >= 270:
            return 360 - angle
        else:
            return angle
