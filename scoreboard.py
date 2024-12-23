from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', True, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
       self.clear()
       self.goto(x=0, y=280)
       self.write(f'Your score is {self.score}', True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

