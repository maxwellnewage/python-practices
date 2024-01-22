from turtle import Turtle


class Score(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)

    def write_result(self, text):
        self.write(text, align="center", font=("Helvetica", 20, "normal"))
