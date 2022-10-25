"""
Crear una calculadora que sume, reste, multiplique y divida
"""


class Calculadora:
    @classmethod
    def suma(cls, n1, n2):
        return n1 + n2

    @classmethod
    def resta(cls, n1, n2):
        return n1 - n2

    @classmethod
    def multi(cls, n1, n2):
        return n1 * n2

    @classmethod
    def div(cls, n1, n2):
        return n1 / n2


print(Calculadora.suma(1, 2))
print(Calculadora.resta(1, 2))
print(Calculadora.multi(1, 2))
print(Calculadora.div(1, 2))
