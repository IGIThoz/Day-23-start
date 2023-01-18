from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-280, 260)
        self.update_sroce_board()

    def update_sroce_board(self):
        self.clear()

        self.write(f"Level: {self.score}",align="left",font=FONT)

    def update_score(self):
        self.score += 1
        self.update_sroce_board()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)
