"""
Ejemplos de docstrings
"""


def hi():
    """Esto es una funcion que imprime un saludo"""
    print("Hello!")


class Car:
    """Clase para crear Autos"""

    def run_engine():
        """Metodo para arrancar el motor"""
        print("rum rum...")


if __name__ == '__main__':
    print(hi.__doc__)
    help(hi)

    help(Car)
    help(Car.run_engine)
