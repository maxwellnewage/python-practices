"""
Crear una calculadora que sume, reste, multiplique y divida
"""


class Calculadora:
    @staticmethod
    def suma(n1, n2):
        return n1 + n2

    @staticmethod
    def resta(n1, n2):
        return n1 - n2

    @staticmethod
    def multi(n1, n2):
        return n1 * n2

    @staticmethod
    def div(n1, n2):
        return n1 / n2


print(Calculadora.suma(1, 2))
print(Calculadora.resta(1, 2))
print(Calculadora.multi(1, 2))
print(Calculadora.div(1, 2))
