import turtle


class HUD:
    def __init__(self):
        self.__score = 0
        self.__high_score = 0
        self.__text = turtle.Turtle()
        self.__text.speed(0)
        self.__text.color("white")
        self.__text.penup()
        self.__text.hideturtle()
        self.__text.goto(0, 260)
        self.__set_text()

    def increment_score(self, score):
        self.__score += score
        self.set_high_score(self.__score)
        self.__set_text()

    def reset_score(self):
        self.set_high_score(self.__score)
        self.__score = 0
        self.__set_text()

    def set_high_score(self, score):
        if score > self.__high_score:
            self.__high_score = score

    def __set_text(self):
        self.__text.clear()
        self.__text.write(
            f"Score: {self.__score} | High Score: {self.__high_score}",
            align="center",
            font=("Courier", 24, "normal")
        )
