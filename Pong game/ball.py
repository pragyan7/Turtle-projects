from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.2
        self.y_move = 0.2
        self.move_speed = 0.1
    
    def move(self):
        '''Moves the ball'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        '''Makes the ball bounce off the walls i.e. y direction'''
        self.y_move *= -1
    
    def bounce_x(self):
        '''Makes the ball bounce off the paddles i.e. x direction'''
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        '''The ball resets back to center'''
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
