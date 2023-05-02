"""
Buscar una serie de posibles nombres por Pipe
"""
import re


def find_names(text):
    names_regex = re.compile(r'Name:(max|tomas|rocky)')

    try:
        return names_regex.search(text).group()
    except AttributeError:
        return None


find_max = find_names('Name:max')
find_tomas = find_names('Name:tomas')
find_voltor = find_names('Name:voltor')

print(find_max)
print(find_tomas)
print(find_voltor)
