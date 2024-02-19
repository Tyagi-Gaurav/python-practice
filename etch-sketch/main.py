import turtle as t

my_turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.setheading(180)
    my_turtle.forward(10)


def turn_left():
    my_turtle.setheading(my_turtle.heading() + 10)


def turn_right():
    my_turtle.setheading(my_turtle.heading() - 10)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

# w - forward
# s - backwards
# a - counter-clockwise
# d - clockwise
# c - clear drawing

screen.exitonclick()
