import time
from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        xcor = self.xcor() + self.x_move
        yxor = self.ycor() + self.y_move
        self.goto(xcor, yxor)
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1