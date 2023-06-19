"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
"""

age_tuple = (5, 10, 15, 20, 25, 30, 40, 50, 66, 80)

for age in age_tuple:
    if age > 20:
        print(age)
