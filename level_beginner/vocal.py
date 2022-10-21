"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""


def is_vowel(character: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if character.lower() in vowels else False


print(is_vowel('A'))
print(is_vowel('b'))
print(is_vowel('I'))
print(is_vowel('u'))
