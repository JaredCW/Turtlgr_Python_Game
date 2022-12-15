from turtle import Turtle
import random
from car_manager import COLORS


# Set some global variables
TRAIN_MOVE_DISTANCE = 20
TRAIN_MOVE_INCREMENT = 15


class TrainManager():
    # Starting attributes
    def __init__(self):
        # This list will hold all the cars that are created
        self.all_trains = []
        self.speed = TRAIN_MOVE_DISTANCE
    
    # Creating the cars
    def create_train(self):
        random_chance = random.randint(1, 30)
        if random_chance == 1:
            new_train = Turtle("square")
            new_train.penup()
            # Set the shape/size of the cars
            new_train.shapesize(stretch_wid=1, stretch_len=4)
            # changes the color of the car to a random choice from our COLORS list
            new_train.color(random.choice(COLORS))
            # generates a new care y-index location
            random_y = random.randint(-240,280)
            # Has the new car go to that location, note the x-index is the same always
            new_train.goto(300, random_y)
            # Add the new car to the all_cars list
            self.all_trains.append(new_train)

    # Set the car movement and speed
    def move_trains(self):
        for train in self.all_trains:
            train.backward(self.speed)

    # Stops all the cars
    def stop_train(self):
        for train in self.all_trains:
            train.backward(0)

    # Increasing the speed when we increase the level
    def increase_speed(self):
        self.speed += TRAIN_MOVE_INCREMENT