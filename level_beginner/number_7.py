"""
Escribe un programa para calcular el porcentaje de números en un rango dado que contienen el dígito 7.

El programa debe tomar una sola entrada entera n que represente el rango máximo (exclusivo), es decir,
el programa calculará el porcentaje de números que contienen un 7 en el rango de 0 a n-1.

https://dev.to/devteam/challenge-counting-numbers-with-7s-33c7
"""


def percentage_of_7(given_range: int):
    seven_amount = 0
    numbers = list(range(given_range))

    for n in numbers:
        if '7' in str(n):
            seven_amount += 1

    return (seven_amount * 100) / len(numbers)


if __name__ == '__main__':
    print(f"{percentage_of_7(10)}%")
