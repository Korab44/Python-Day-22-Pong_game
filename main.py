from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()



screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()


















screen.exitonclick()