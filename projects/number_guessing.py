"""
Adivina el número que estoy pensando.
"""

from random import choice

# { porcentaje de cercanía : puntaje asignado }
score_by_prob = [
    {
        'percentage': 100,
        'score': 10
    },
    {
        'percentage': 80,
        'score': 7
    },
    {
        'percentage': 50,
        'score': 4
    }
]

# cada grado de dificultad tiene un rango mayor de números
# pero también un bonificador que multiplicará la puntuación
difficulty = [
    {
        'name': 'fácil',
        'numbers': 10,
        'bonus': 1
    },
    {
        'name': 'intermedio',
        'numbers': 50,
        'bonus': 2
    },
    {
        'name': 'difícil',
        'numbers': 100,
        'bonus': 3
    }
]

# Si fallas el número, pierdes una vida.
# current_life lleva la cuenta, pero max_life permite reiniciar el juego
max_life = 3
current_life = 3

min_score = 0
current_score = 0


def show_difficulty():
    for i, d in enumerate(difficulty):
        print(
            f"{i + 1}. "
            f"En la dificultad {d['name']} "
            f"tienes que adivinar entre {d['numbers']} números, "
            f"pero tendrás un multiplicador de puntaje de {d['bonus']}x"
        )


def select_difficulty():
    diff = int(input("¿Qué nivel de dificultad seleccionarás?: "))
    return difficulty[diff - 1]


def set_pc_number(diff):
    return choice(range(1, diff['numbers'] + 1))


def get_result(pc_number, user_number, diff):
    """
    para obtener un porcentaje de distancias
    necesito dividir el más chico por el más grande
    """
    division = (user_number / pc_number) \
        if user_number < pc_number else pc_number / user_number

    percentage_btw = division * 100
    score = 0
    for s in score_by_prob:
        if percentage_btw >= s['percentage']:
            score = s['score'] * diff['bonus']
            break

    return {'score': score, 'prob': int(percentage_btw)}


def loose(pc_number):
    global current_life
    current_life -= 1
    print(f"Has perdido! El número era {pc_number}.")
    print(f"Te quedan {current_life} vidas.")


def win(result, pc_number):
    global current_score
    current_score += result['score']
    print(
        f"¡Te has acercado con una probabilidad del {result['prob']}% "
        f"y un score de {result['score']}!"
    )
    print(f"El número de la PC era {pc_number}")
    print(f"Tu puntaje actual es: {current_score}")


def reset():
    global current_score, current_life
    print(f"Juego terminado! Tu score final fue de {current_score}")
    current_score = min_score
    current_life = max_life


def play():
    print("---------------------")
    print("-- Number Guessing --")
    print("---------------------")
    show_difficulty()
    current_difficulty = select_difficulty()

    while current_life > 0:
        pc_number = set_pc_number(current_difficulty)
        user_number = int(
            input(
                f"Adivina el número que estoy pensando "
                f"(1 al {current_difficulty['numbers']}): "
            )
        )
        result = get_result(pc_number, user_number, current_difficulty)
        if result['score'] == 0:
            loose(pc_number)
        else:
            win(result, pc_number)

    reset()


play()
