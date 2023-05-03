"""
Detectar una lista de vocales mayúsculas y minúsculas en un string.
"""
import re

vowel_regex = re.compile(r'[aeiouAeiou]')

print(vowel_regex.findall('Quiero las vocales de esta cadena'))
