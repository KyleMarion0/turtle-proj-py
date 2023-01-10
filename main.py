from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("purple")

for shape1 in range(3):
    tim.forward(100)
    tim.right(120)

for shape2 in range(4):
    tim.forward(100)
    tim.right(90)

for shape3 in range(5):
    tim.forward(100)
    tim.right(72)

for shape4 in range(6):
    tim.forward(100)
    tim.right(60)

for shape5 in range(7):
    tim.forward(100)
    tim.right(51.43)

for shape6 in range(8):
    tim.forward(100)
    tim.right(45)

for shape7 in range(9):
    tim.forward(100)
    tim.right(40)

screen = Screen()
screen.exitonclick()