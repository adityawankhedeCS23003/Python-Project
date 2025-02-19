import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1=Player()
car=CarManager()
score=Scoreboard()


screen.listen()
screen.onkeypress(p1.go,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #collision detection of car and turtle
    for cars in car.all_cars:
        if cars.distance(p1) < 20:
            p1.game_over()
            game_is_on=False

    #next level
    if p1.at_finish():
        p1.starting_pos()
        car.increase_speed()
        score.increase_score()


screen.mainloop()





