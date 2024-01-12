from turtle import Turtle, Screen, colormode
import colorgram
from random import choice

colormode(255)

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []
for color in colors:
    rgb_colors.append(
        (
            color.rgb.r,
            color.rgb.g,
            color.rgb.b
        )
    )

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.pendown()
    turtle.dot(20, choice(rgb_colors))
    turtle.penup()
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = Screen()
screen.exitonclick()