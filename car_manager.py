from turtle import Turtle
import random


# Set some global variables
# Car color list
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        # This list will hold all the cars that are created
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    
    # Creating the cars
    def create_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Changes the color of the car to a random choice from our COLORS list
            # ! THIS IS A RANDOM CHOICE GENERATOR USE THIS DEAR GOD ASDFJKL!
            new_car.color(random.choice(COLORS))
            # Generates a new car y-index location, moves to that location
            random_y = random.randint(-240,280)
            new_car.goto(300, random_y)
            # Adds the new car to the all_cars list
            self.all_cars.append(new_car)

    # Set the car movement and speed
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    # Increasing the speed when we increase the level
    def increase_speed(self):
        self.speed += MOVE_INCREMENT