from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.pensize(0.1)
tim.speed("fastest")

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)
        tim.hideturtle()

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
