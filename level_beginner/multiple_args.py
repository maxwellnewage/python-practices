"""
Definir una función que soporte múltiples argumentos.
"""


def name_likes_colors(name, *colors):
    print(f"A {name} le gustan los siguientes colores:")
    for c in colors:
        print(f"- {c}")


print(name_likes_colors("Max", "azul"))
print(name_likes_colors("Tomas", "azul", "verde"))
print(name_likes_colors("Clark", "azul", "verde", "rojo"))
