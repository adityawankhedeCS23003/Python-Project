import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars=[]
        self.car_speed=MOVE_INCREMENT


    def create_car(self):

        random_car=random.randint(1,6)
        if random_car == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)


    def increase_speed(self):
        self.car_speed +=1


    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    

    

    
