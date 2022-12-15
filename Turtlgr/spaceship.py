from turtle import Screen, Turtle
import random
from car_manager import COLORS

# Create and register spaceship shape
screen = Screen()
shape = ((0,0), (-5,0), (-6,8), (-14,8), (-15,0), (-20,0), (-15,-12), (-5,-12))
screen.register_shape("spaceship", shape)

# Set some global variables
SPACESHIP_MOVE_DISTANCE = 15
SPACESHIP_MOVE_INCREMENT = 8


class SpaceshipManager():
    # Starting attributes
    def __init__(self):
        # This list will hold all the cars that are created
        self.all_spaceship = []
        self.speed = SPACESHIP_MOVE_DISTANCE
    
    # Creating the ships
    def create_ship(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_ship = Turtle("spaceship")
            new_ship.penup()
            # Set the shape/size of the spaceships
            new_ship.shapesize(stretch_wid=2, stretch_len=1)
            # changes the color of the car to a random choice from our COLORS list
            # ! THIS IS A RANDOM CHOICE GENERATOR USE THIS DEAR GOD ASDFJKL!
            new_ship.color(random.choice(COLORS))
            # generates a new care y-index location
            random_y = random.randint(-240,280)
            # Has the new car go to that location, note the x-index is the same always
            new_ship.goto(300, random_y)
            random_heading = random.randint(1,2)
            if random_heading == 1:
                new_ship.setheading(135)
                new_ship.settiltangle(-45)
            else:
                new_ship.setheading(225)
                new_ship.settiltangle(225)
            # Add the new car to the all_cars list
            self.all_spaceship.append(new_ship)

    # Set the ship movement, angle and speed. Changes direction based on location
    def move_ship(self):
        for ships in self.all_spaceship:
            y_cor = Turtle.ycor(ships)
            ships.forward(self.speed)
            if y_cor >= 270:
                ships.setheading(225)
                ships.settiltangle(225)
            if y_cor <= -230:
                ships.setheading(135)
                ships.settiltangle(315)

    # Increasing the speed when we increase the level
    def increase_speed(self):
        self.speed += SPACESHIP_MOVE_INCREMENT