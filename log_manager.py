from turtle import Turtle
import random
from car_manager import STARTING_MOVE_DISTANCE

class LogManager():
    def __init__(self):
        self.all_logs = []
        self.log_speed = STARTING_MOVE_DISTANCE
   
    def create_logs(self):
        random_chance = random.randint (1, 10)
        if random_chance == 1:
            new_logs = Turtle("square")
            new_logs.penup()
            new_logs.shapesize(stretch_wid=1, stretch_len= 4)
            new_logs.color("brown")
            random_pos = random.randint (1, 2)
            if random_pos == 1:
                new_logs.goto(300, 90)
            else:
                new_logs.goto(300, 110)
            self.all_logs.append(new_logs)

    def move_logs(self):
        for log in self.all_logs:
            log.backward(self.log_speed)
