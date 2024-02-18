import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)

colors = ["CornflowerBlue", "red", "blue", "green", "black", "brown", "IndianRed", "DarkOrchid", "LightSeaGreen",
          "wheat", "SlateGray"]

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def draw_square(turtle, pen_color):
    turtle.pencolor(pen_color)

    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


def draw_dashed_line(turtle, pen_color):
    turtle.pencolor(pen_color)
    for _ in range(20):
        turtle.forward(5)
        turtle.up()
        turtle.forward(5)
        turtle.down()


def draw_triangle(turtle, pen_color):
    turtle.shape("turtle")
    turtle.pencolor(pen_color)
    turtle.fillcolor("red")

    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)


def draw_shape(turtle, pen_color, number_of_sides):
    turtle.pencolor(pen_color)
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_different_shapes(turtle):
    for sides in range(3, 11):
        draw_shape(turtle, random.choice(colors), sides)


def random_walk(turtle):
    turtle.pensize(15)
    turtle.speed("fastest")
    for _ in range(0, 50):
        turtle.setheading(random.choice(directions))
        turtle.pencolor(random_color())
        turtle.forward(30)


def spirograph(turtle):
    turtle.speed("fastest")
    angle = 5
    times = int(360 / angle)
    for _ in range(times):
        turtle.setheading(turtle.heading() + angle)
        turtle.pencolor(random_color())
        turtle.circle(100)


# draw_square(my_turtle, "red")
# draw_triangle(my_turtle, "blue")
# draw_dashed_line(my_turtle, "green")
# draw_different_shapes(my_turtle)
# random_walk(my_turtle)
# spirograph(my_turtle)


screen = t.Screen()
screen.exitonclick()
