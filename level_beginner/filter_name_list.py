"""
Definir una lista con un conjunto de nombres,
imprimir la cantidad que comienzan con una letra seleccionada por el usuario.
"""


def list_name_filter(names: list[str], first_letter):
    names_result = []
    for name in names:
        if first_letter == name[0]:
            names_result.append(name)

    return names_result


if __name__ == '__main__':
    print(list_name_filter(["Max", "Tomas", "Rocky", "Mendel", "Misty"], "M"))
