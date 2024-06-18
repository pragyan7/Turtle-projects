from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Function to draw a colorful spiral
def draw_colorful_spiral():
    distance = 1  # Initial distance to move forward
    for _ in range(200):  # Adjust the range for longer/shorter spirals
        tim.color(random_color())  # Set a random color
        tim.forward(distance)
        tim.right(60)  # Adjust the angle for different spiral tightness
        distance += 1  # Increment the distance

draw_colorful_spiral()

my_screen = Screen()
my_screen.exitonclick()
my_screen.setup(width=800, height=600)
