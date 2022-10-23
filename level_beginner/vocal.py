"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

from globals import vowels


def is_vowel(character: str):
    return True if character.lower() in vowels else False


def main():
    print(is_vowel('A'))
    print(is_vowel('b'))
    print(is_vowel('I'))
    print(is_vowel('u'))
