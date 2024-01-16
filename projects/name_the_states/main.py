import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
t.bgpic("blank_states_img.gif")

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput("Guess the state", "What's another state's name?").lower()

    states = pd.read_csv("50_states.csv")
    guess_state = states[states.state.str.lower() == answer_state.lower()]

    if answer_state == "exit":
        break

    if not guess_state.empty:
        marker = t.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(guess_state.x), int(guess_state.y))
        t.write(guess_state.state.item())
        guessed_states.append(guess_state)


screen.exitonclick()
