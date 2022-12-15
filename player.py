from turtle import Screen, Turtle

STARTING_POSTION = (0, -280)
TURTLE_MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Passing in the Turtle Class here lets our Player class have all the same attributes and methods as the Turtle Class
    def __init__(self):
        # The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.
        super().__init__()
        # NOW we can access everything we need from the turtle class
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.right(270)
        self.goto(STARTING_POSTION)

    # Allow for forward movement
    def move_forward(self):
        new_y = self.ycor() + TURTLE_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # Left movement
    def move_left(self):
        new_left = self.xcor() - TURTLE_MOVE_DISTANCE
        self.goto(new_left, self.ycor())

    # Right movement
    def move_right(self):
        new_right = self.xcor() + TURTLE_MOVE_DISTANCE
        self.goto(new_right, self.ycor())

    # Reset the turtle
    def reset_turtle(self):
        self.goto(STARTING_POSTION)

    # Marks the finish line and returns a Boolean (needed to progress the game)
    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False