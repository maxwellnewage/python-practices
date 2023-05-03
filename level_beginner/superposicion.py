"""
Definir una función superposicion() que tome dos listas y
devuelva True si tienen al menos 1 miembro en común o
devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.
"""


def superposicion(list_1, list_2):
    same_member = False
    for l1 in list_1:
        for l2 in list_2:
            if l1 == l2:
                same_member = True
                break
    return same_member


if __name__ == '__main__':
    print(superposicion([1, 2], [1, 3]))
    print(superposicion([1, 2], [4, 3]))
    print(superposicion([1, 2, 3, 4], [1, 5, 3]))
