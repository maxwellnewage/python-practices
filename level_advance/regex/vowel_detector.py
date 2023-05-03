"""
Detectar una lista de vocales mayúsculas y minúsculas en un string.
"""
import re


def find_vowels(phrase):
    vowel_regex = re.compile(r'[aeiouAeiou]')
    return vowel_regex.findall(phrase)


if __name__ == '__main__':
    print(find_vowels('Quiero las vocales de esta cadena'))

