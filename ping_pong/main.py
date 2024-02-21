import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

left_paddle = Paddle(550, 0)
right_paddle = Paddle(-550, 0)
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
