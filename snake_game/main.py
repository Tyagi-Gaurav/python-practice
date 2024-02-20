import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
snake.create()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.increase_length()
    elif snake.hit_any_obstacle():
        game_is_on = False
        text = Turtle()
        text.color("white")
        text.hideturtle()
        text.penup()
        text.write(f"Game Over!", align="center", font=('Arial', 24, 'normal'))


screen.exitonclick()
