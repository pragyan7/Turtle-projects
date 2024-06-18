from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        '''Updates the scoreboard'''
        self.clear()
        # Left player score
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("courier", 30, "bold"))
        # Right player score
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("courier", 30, "bold"))
    
    def l_point(self):
        '''Increases the score by 1 when left player scores'''
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        '''Increases the score by 1 when right player scores'''
        self.r_score += 1
        self.update_scoreboard()
