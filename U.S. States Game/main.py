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

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]   # Getting hold of the row
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    # t.write(state_data.state.item())

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()   # To keep the screen open even if the code has finished running
screen.exitonclick()
