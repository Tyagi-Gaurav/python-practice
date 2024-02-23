import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
state_data = pandas.read_csv("50_states.csv")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(width=750, height=500)

guessed_states = []
title = "Guess the state"

# Read from CSV and get coordinates for all states
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state's  name?")
    state_frame = state_data[state_data.state.str.lower() == answer_state.lower()]

    if answer_state == "exit":
        break

    if state_frame.empty:
        print(f"No state found {answer_state}")
    else:
        answer = state_frame["state"].item()
        guessed_states.append(answer)
        title = f"{len(guessed_states)}/50 States Correct"
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()

        t.goto(int(state_frame.x), int(state_frame.y))
        t.write(answer)

# Write states to learn in a separate CSV
rem_states = []
for state in state_data.values.tolist():
    if state[0] not in guessed_states:
        rem_states.append(state[0])

data_dict = {
    "states": rem_states
}
df = pandas.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
