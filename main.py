from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"]
direction = [0, 90, 180, 270]

tim.pensize(15)
tim.speed(10)
for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
