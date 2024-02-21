import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score_board import Scoreboard

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

left_paddle = Paddle(-550, 0)
right_paddle = Paddle(550, 0)
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

score_board = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 550:
        ball.reset_position()
        score_board.update_left()

    if ball.xcor() < -550:
        ball.reset_position()
        score_board.update_right()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 520) or (
            ball.distance(left_paddle) < 50 and ball.xcor() > -550):
        ball.bounce_x()
        ball.increase_speed()

screen.exitonclick()
