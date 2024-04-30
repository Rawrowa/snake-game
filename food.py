from turtle import Turtle
from random import randrange

TOP = 260


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        rng_x = randrange(-280, TOP, 20)
        rng_y = randrange(-280, TOP, 20)
        self.goto(rng_x, rng_y)

    def relocate(self):
        rng_x = randrange(-280, TOP, 20)
        rng_y = randrange(-280, TOP, 20)
        self.goto(rng_x, rng_y)
