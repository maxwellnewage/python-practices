"""
Definir una función que calcule la longitud de una lista o una cadena dada.
"""


def calc_list_or_string(value):
    size = 0
    for _ in value:
        size += 1
    return size


print(calc_list_or_string([1, 4, "bla", True]))
print(calc_list_or_string("esto es una cadena"))
