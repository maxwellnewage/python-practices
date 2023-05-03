"""
Crear una clase persona que se pueda describir con __str__
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} {self.__age}"


if __name__ == '__main__':
    maxwell = Person("Maxwell", "Tompson", 32)
    print(maxwell)
