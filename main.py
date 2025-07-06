from turtle import Screen,Turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
map_us = Turtle()  # Created a t called map_us
map_us.shape(img)  # Gave it the shape of us img gif

data = pd.read_csv('50_states.csv')
all_states = (data['state']).to_list()

guessed_state = []


while len(guessed_state) < 50 :
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Guessed",prompt="What's another state name?")

    if answer is None:
        continue

    answer = answer.title()

    if answer == 'Exit':
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)

        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break

    for state in all_states:
        if answer == state:
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data['state'] == answer]
            x_cor = int(state_data.x)
            y_cor = int(state_data.y)
            t.goto(x_cor,y_cor)
            t.write(answer)
            guessed_state.append(answer)

screen.exitonclick()