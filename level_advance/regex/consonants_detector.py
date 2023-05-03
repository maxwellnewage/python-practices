"""
Detectar una lista de consonantes en un string.
"""
import re


def find_consonants(phrase):
    # el signo ^ implica negación: en este caso devuelve todas las
    # que no son vocales, por lo tanto, consonantes
    consonants_regex = re.compile(r'[^aeiouAEIOU]')
    return consonants_regex.findall(phrase)


if __name__ == '__main__':
    print(find_consonants('Quiero las consonantes de esta cadena'))

