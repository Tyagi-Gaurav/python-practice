import time
import random
from turtle import Screen
from game_turtle import MyTurtle
from score_board import Scoreboard

from car import CarManager

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Squish")
screen.colormode(255)
screen.tracer(0)
screen.listen()

score_board = Scoreboard()
car_manager = CarManager(800, 600)
keep_going = True
my_turtle = MyTurtle()
screen.onkey(my_turtle.move_up, "Up")

while keep_going:
    chance = random.randint(1, 6)
    screen.update()
    time.sleep(car_manager.car_speed)

    car_manager.move_all_cars()

    if chance == 1:
        car_manager.generate_cars(4)

    if car_manager.any_car_collides_with(my_turtle):
        keep_going = False
        score_board.game_over()
        break

    if my_turtle.has_reached_top():
        car_manager.increment_level()
        my_turtle.reset_position()
        score_board.update()

screen.exitonclick()
