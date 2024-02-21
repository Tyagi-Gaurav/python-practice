from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed(5)
        # self.setheading(10)
        self.penup()
        self.increment_x = 20
        self.increment_y = 20
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.increment_x, self.ycor() + self.increment_y)
        if self.ycor() >= 370 or self.ycor() <= -370:  # Hitting the wall
            self.bounce_y()
            # self.setheading(180 - self.__to_quadrant_angle())
            # self.increment = -1 * self.increment

    def __to_quadrant_angle(self):
        angle = self.heading()
        if 180 < angle < 270:
            return 270 - angle
        elif angle >= 270:
            return 360 - angle
        else:
            return angle

    def bounce_y(self):
        self.increment_y = -1 * self.increment_y

    def bounce_x(self):
        self.increment_x = -1 * self.increment_x

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed = self.move_speed * 0.9
