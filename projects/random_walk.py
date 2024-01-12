from turtle import Turtle, Screen, colormode
from random import choice, randint

directions = [0, 90, 180, 270]

turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
colormode(255)


def random_color():
    return (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )


for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
