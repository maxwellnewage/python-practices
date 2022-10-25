"""
Crear una calculadora que sume, reste, multiplique y divida
"""


class Calculadora:
    def __init__(self, n1, n2):
        # el doble guion bajo indica que el atributo es privado
        self.__n1 = n1
        self.__n2 = n2

    def suma(self):
        return self.__n1 + self.__n2

    def resta(self):
        return self.__n1 - self.__n2

    def multi(self):
        return self.__n1 * self.__n2

    def div(self):
        return self.__n1 / self.__n2


calc = Calculadora(1, 2)
print(calc.suma())
print(calc.resta())
print(calc.multi())
print(calc.div())
