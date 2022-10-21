"""
Definir un histograma procedimiento()
que tome una lista de números enteros e imprima un histograma en la pantalla.
"""


def procedimiento(numbers):
    stars = ""
    for n in numbers:
        stars += "*" * n + "\n"
    return stars


print(procedimiento([4, 9, 7]))
print(procedimiento([1, 2, 3, 4, 5, 2, 2]))
