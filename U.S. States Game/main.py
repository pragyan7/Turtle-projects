from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
screen = Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''Check if answer_state is one of the states in 50_states.csv'''
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", 
                                    prompt = "What's another State name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]   # Getting hold of the row
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    # t.write(state_data.state.item())
