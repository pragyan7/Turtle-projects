from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''This creates a snake made up of three segments'''
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        '''This method helps create a snake made up of three segments'''
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    def add_segment(self, position):
        '''Adds a new segment to the end segment of the snake'''
        turtle = Turtle(shape = "square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
    
    def extend(self):
        '''Extends the length of snake by adding a segment'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''This method makes the snake move in the playground'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        '''This method moves up the snake except when its facing down'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        '''This method moves down the snake except when its facing up'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''This method moves the snake to the left except when its facing right'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''This method moves the snake to the right except when its facing left'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
