"""
Armar una calculadora que sobreescriba los métodos de la primera
"""

from calculadora import Calculadora


class CalculadoraDescriptiva(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    # super().suma() va a retornar el valor del padre
    def suma(self):
        return f"{self.n1} + {self.n2} = {super().suma()}"

    def resta(self):
        return f"{self.n1} - {self.n2} = {super().resta()}"


print(CalculadoraDescriptiva(1, 2).suma())
print(CalculadoraDescriptiva(1, 2).resta())
