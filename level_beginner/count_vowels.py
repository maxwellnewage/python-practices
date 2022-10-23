"""
Crear una función contar_vocales()
"""

from vocal import is_vowel


def contar_vocales(word: str):
    vocals = 0
    for w in word:
        if is_vowel(w):
            vocals += 1

    return vocals


print(contar_vocales("abecedario"))
print(contar_vocales("palabra"))
print(contar_vocales("sistema"))
print(contar_vocales("aaa"))
