"""
Armar una calculadora que sobreescriba los métodos de la primera
"""

from calculator import Calculadora


class CalculadoraDescriptiva(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    # super().suma() va a retornar el valor del padre
    def suma(self):
        return f"{self.n1} + {self.n2} = {super().suma()}"

    def resta(self):
        return f"{self.n1} - {self.n2} = {super().resta()}"


if __name__ == '__main__':
    print(CalculadoraDescriptiva(1, 2).suma())
    print(CalculadoraDescriptiva(1, 2).resta())
