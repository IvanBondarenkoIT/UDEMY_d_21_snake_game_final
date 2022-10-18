from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refrash()

    def refrash(self):
        rand_x = random.randint(-280, 280)
        rand_Y = random.randint(-280, 280)
        self.goto(rand_x, rand_Y)