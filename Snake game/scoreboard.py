from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Updates the score once the food is consumed'''
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    
    def game_over(self): # Writing it here cuz we want to see the score and clear() is not called yet
        '''Ends the game'''
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        '''Increases the score by 1 once food is consumed'''
        self.score += 1
        self.clear()
        self.update_scoreboard()
