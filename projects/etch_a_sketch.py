import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_up():
    turtle.forward(10)


def move_left():
    turtle.setheading(turtle.heading() + 10)
    turtle.forward(10)


def move_down():
    turtle.backward(10)


def move_right():
    turtle.setheading(turtle.heading() - 10)
    turtle.forward(10)


screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=turtle.reset)

screen.exitonclick()
