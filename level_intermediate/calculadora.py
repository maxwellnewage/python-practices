"""
Crear una calculadora que sume, reste, multiplique y divida
"""


class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        return self.n1 + self.n2

    def resta(self):
        return self.n1 - self.n2

    def multi(self):
        return self.n1 * self.n2

    def div(self):
        return self.n1 / self.n2


if __name__ == "__main__":
    calc = Calculadora(1, 2)
    print(calc.suma())
    print(calc.resta())
    print(calc.multi())
    print(calc.div())
