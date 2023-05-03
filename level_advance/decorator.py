"""
Función que suma dos números mediante un decorator
"""


def calculate(suma):
    def wrapper(*args, **kwargs):
        print("---Inicio Función que suma números---")
        suma(*args, **kwargs)
        print("---Fin Función que suma números---")
    return wrapper


@calculate
def sum_2_nums(n1, n2):
    print(f"La suma de {n1} y {n2} es {n1 + n2}")


if __name__ == '__main__':
    sum_2_nums(1, 2)
