# import colorgram

# rgb_colors = []
# # Extract 30 colors from an image.
# colors = colorgram.extract('image.jfif', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

'''The code above gave the followin list of colors which we will use for creating Hirst spot painting'''
#color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), 
            #   (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), 
            #   (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), 
            #   (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
'''The above color list was showing error, instead I am gonna use random colors'''

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225) # To move the turtle close to bottom left. The value is between 180 and 270
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

def random_color():
    return (random.random(), random.random(), random.random())

for dot_count in range(1, num_of_dots+1):
    tim.dot(15, random_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90) #Changes the head towards North
        tim.forward(50) #Goes up by 50
        tim.setheading(180) #Changes the head towards West
        tim.forward(500) #Goes to the left. Each pace is 50 and we need to have 10 dots each row. So, 50x10
        tim.setheading(0) #Changes the head towards East

my_screen = Screen()
my_screen.exitonclick()
