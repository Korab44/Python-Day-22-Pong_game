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
        self.move_speed = 0.1

    def move(self):
        xcor = self.xcor() + self.x_move
        yxor = self.ycor() + self.y_move
        self.goto(xcor, yxor)
    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9