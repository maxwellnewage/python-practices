from turtle import Screen
from score import Score
from race import Race

SCREEN_SCALE = 1.2
WIDTH = 500 * SCREEN_SCALE
HEIGHT = 400 * SCREEN_SCALE
screen = Screen()
screen.setup(WIDTH, HEIGHT)
user_bet = screen.textinput("Make your bet", "Enter a color: ")
text_result = Score((0, HEIGHT / 2.5))
text_winner_turtle = Score((0, HEIGHT / 3))
race = Race(SCREEN_SCALE)

if user_bet:
    race.start()
    race.move_turtles(user_bet, text_result, text_winner_turtle)

screen.exitonclick()
