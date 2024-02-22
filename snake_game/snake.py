import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
turtle.colormode(255)


def get_new_segment():
    t = Turtle("square")
    t.color(random_color())
    t.penup()
    return t


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


class Snake:
    def __init__(self):
        self.X_MOVE_DIRECTION = 20
        self.Y_MOVE_DIRECTION = 0
        self.segments = None
        self.head = None
        self.tail = None

    def move(self):
        seg_index = len(self.segments) - 1
        while seg_index > 0:
            segment1 = self.segments[seg_index]
            segment2 = self.segments[seg_index - 1]
            segment1.goto(segment2.xcor(), segment2.ycor())
            seg_index -= 1

        self.head.forward(MOVE_DISTANCE)

    def create(self):
        self.segments = []
        start = -10

        for seg_index in range(3):
            t = get_new_segment()
            t.color(random_color())
            t.goto(start - seg_index * 20, t.ycor())
            self.segments.append(t)

        self.tail = self.segments[2]
        self.head = self.segments[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def _is_close_to_wall(self):
        return (self.head.xcor() > 295 or  # right
                self.head.ycor() > 295 or  # top
                self.head.ycor() < -295 or  # bottom
                self.head.xcor() < -295)  # left

    def increase_length(self):
        new_seg = get_new_segment()
        new_seg.goto(self.tail.xcor() + 20, self.tail.ycor())
        self.tail = new_seg
        self.segments.append(new_seg)

    def _hitting_itself(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False

    def hit_any_obstacle(self):
        return self._hitting_itself() or self._is_close_to_wall()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create()
