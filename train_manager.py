from turtle import Turtle
import random
from car_manager import COLORS


TRAIN_MOVE_DISTANCE = 20
TRAIN_MOVE_INCREMENT = 2


class TrainManager():
    def __init__(self):
        self.all_trains = []
        self.speed = TRAIN_MOVE_DISTANCE
    
    def create_train(self):
        random_chance = random.randint(1, 30)
        if random_chance == 1:
            new_train = Turtle("square")
            new_train.penup()
            new_train.shapesize(stretch_wid=1, stretch_len=4)
            new_train.color(random.choice(COLORS))
            random_y = random.randint(-240,280)
            # This loop prevents spawn inside the River area.
            # TODO: River function. This loop is commented out until reimplemented.
            # while (random_y >= 80 and random_y <= 140):
            #     random_y = random.randint(-240,280)
            new_train.goto(300, random_y)
            self.all_trains.append(new_train)

    def move_trains(self):
        for train in self.all_trains:
            train.backward(self.speed)

    def increase_speed(self):
        self.speed += TRAIN_MOVE_INCREMENT