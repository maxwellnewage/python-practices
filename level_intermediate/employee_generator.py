"""
Crear un programa que genere empleados con nombre, apellido, rol y salario,
previamente con una clase Person como padre.
"""


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def full_name(self):
        return self.__first_name + " " + self.__last_name


class Employee(Person):
    def __init__(self, first_name, last_name, role, salary):
        super().__init__(first_name, last_name)
        self.__role = role
        self.__salary = salary

    def info(self):
        return f"El empleado {self.full_name()} tiene el rol de {self.__role} con un salario de ${self.__salary}"


maxwell = Person("Maxwell", "Tompson")
print(maxwell.full_name())
tomas = Employee("Tomas", "Dickens", "Developer", 12000)
print(tomas.info())
