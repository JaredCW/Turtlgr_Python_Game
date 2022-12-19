from turtle import Turtle
import random



class RiverManager():
    def __init__(self):
        pass
    
    def create_river(self):
        river = Turtle("square")
        river.penup()
        river.shapesize(stretch_wid=2, stretch_len=36)
        river.color("blue")
        river.goto(0, 100)
