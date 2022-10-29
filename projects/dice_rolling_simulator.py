"""
Simulador de tirada de dados.
"""

from random import choice


def dice(quantity):
    for q in range(quantity):
        # son dados de 6, pero el último es n - 1
        roll = choice(range(1, 7))
        print(f"Tu dado #{q + 1} salió {roll}")


print("----------------------------")
print("-- Dice Rolling Simulator --")
print("----------------------------")
dice(int(input("Cuantos dados usaremos?: ")))

