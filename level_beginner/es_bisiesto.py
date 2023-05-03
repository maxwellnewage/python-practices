"""
Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100; también por 400.
"""


def es_bisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(es_bisiesto(1900))
    print(es_bisiesto(1992))
    print(es_bisiesto(1996))
    print(es_bisiesto(2020))
    print(es_bisiesto(2022))
