from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_fisnish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False