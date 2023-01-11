from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_values = (r, g, b)
    return rgb_values

direction = [0, 90, 180, 270]

tim.pensize(15)
tim.speed(10)
for _ in range(250):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(direction))

screen.exitonclick()
