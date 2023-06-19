"""
Detectar una lista de vocales mayúsculas y minúsculas en un string.
"""
import re


def find_vowels(phrase):
    vowel_regex = re.compile(r'[aeiou]')
    return vowel_regex.findall(phrase)


def find_vowels_ignore_case(phrase):
    return re.compile(r'[aeiou]', re.IGNORECASE).findall(phrase)


if __name__ == '__main__':
    print(find_vowels('Quiero las vOcalEs de Esta cadena'))
    print(find_vowels_ignore_case('Quiero las vOcalEs de Esta cadenA'))
