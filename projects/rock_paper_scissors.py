"""
El famoso juego "Piedra, Papel o Tijeras".
"""

from random import choice

ROCK = 'Piedra'
PAPER = 'Papel'
SCISSORS = 'Tijeras'

choice_list = [ROCK, PAPER, SCISSORS]

player_score = 0
pc_score = 0

is_playing = True


def calculate_score(player_choice, pc_choice):
    if player_choice == pc_choice:
        score = 0
    elif player_choice == ROCK and pc_choice == SCISSORS:
        score = 1
    elif player_choice == PAPER and pc_choice == ROCK:
        score = 1
    elif player_choice == SCISSORS and pc_choice == PAPER:
        score = 1
    else:
        score = -1

    return score


def get_pc_choice():
    return choice([ROCK, PAPER, SCISSORS])


def get_result(score, player_choice, pc_choice):
    global player_score, pc_score
    print("-----------------------")
    if score == 1:
        player_score += 1
        print("Ganaste!")
    elif score == -1:
        pc_score += 1
        print("Perdiste :(")
    else:  # score == 0
        print("Es un empate!")

    print(f"Elegiste {player_choice} y PC eligió {pc_choice}")
    print(f"[Tú] {player_score} - {pc_score} [PC]")
    print("-----------------------")


def play():
    global is_playing
    print("-----------------------------")
    print("-- Piedra, Papel o Tijeras --")
    print("-----------------------------")
    while is_playing:
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        print("4. Salir")

        player_int_choice = int(input("Que vas a elegir este turno?: "))

        if player_int_choice == 4:
            is_playing = False
        else:
            player_choice = choice_list[player_int_choice - 1]
            pc_choice = get_pc_choice()
            score = calculate_score(player_choice, pc_choice)
            get_result(score, player_choice, pc_choice)


play()
