"""
Leer un archivo JSON de colores y listarlo
"""

import json

FILE = "resources/colors_code.json"

json_file = open(FILE)
json_colors = json.load(json_file)

for c in json_colors:
    print(f'Color: {c["color"]} | Code: {c["value"]}')

json_file.close()
