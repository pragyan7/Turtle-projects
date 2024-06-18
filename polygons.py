from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)

colors = ["DeepPink4", "chartreuse3", "goldenrod1", "DodgerBlue3", "firebrick3", "SlateBlue3", "purple2", "yellow2", "salmon3", "RoyalBlue1", "SpringGreen2", "midnightblue" ]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for s in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(s)

my_screen = Screen()
my_screen.exitonclick()
