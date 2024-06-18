from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")

def random_color():
    return(random.random(), random.random(), random.random())

def check_boundary():
    x, y = tim.pos()
    if x < -390 or x > 390 or y < -290 or y > 290:
        tim.right(180)

for _ in range(1000):
    tim.color(random_color())
    tim.forward(30)
    check_boundary()
    tim.right(random.choice([0, 90, 180, 270]))



my_screen = Screen()
my_screen.exitonclick()
my_screen.setup(width=800, height=600)
