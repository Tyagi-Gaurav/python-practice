from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Enter any rainbow color: ")

colors = ["red", "orange", "yellow", "violet", "indigo", "blue", "green"]

turtles = []

start_y = -80

for turtle_index in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-240, start_y + turtle_index * 30)
    turtles.append(t)
    t.pendown()

race_on = True
winner = user_bet

while race_on:
    for turtle_index in range(len(colors)):
        t = turtles[turtle_index]
        t.penup()
        t.forward(random.randint(1, 10))
        t.pendown()

        if t.xcor() > 220:
            race_on = False
            winner = colors[turtle_index]

if winner == user_bet:
    print (f"You Win! Winner is {winner}.")
else:
    print (f"You Lose! Winner is {winner}.")

