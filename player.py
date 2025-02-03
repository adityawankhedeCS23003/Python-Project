from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("turtle")
        self.penup()
        self.starting_pos()
        self.setheading(90)

    def go(self):
        self.fd(MOVE_DISTANCE)


    def starting_pos(self):
        self.goto(STARTING_POSITION)
    
    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("courier",50,"bold"))
    
    def at_finish(self):
        if self.ycor() >280:
            return True
        else:
            return False
    
