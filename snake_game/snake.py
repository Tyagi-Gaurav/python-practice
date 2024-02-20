from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.X_MOVE_DIRECTION = 20
        self.Y_MOVE_DIRECTION = 0
        self.segments = None
        self.head = None

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
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(start + seg_index * 20, t.ycor())
            self.segments.append(t)

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
