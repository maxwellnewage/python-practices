"""
Contar vocales de una frase y generar un diccionario con clave en cada vocal.
"""
from level_advance.regex.vowel_detector import find_vowels

phrase = "Quiero las vocales de esta cadena"
vowels = find_vowels(phrase)
dict_vowel_counter = {}

for v in vowels:
    if v in dict_vowel_counter:
        dict_vowel_counter[v] += 1
    else:
        dict_vowel_counter[v] = 1

if __name__ == '__main__':
    print(dict_vowel_counter)
