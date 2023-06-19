"""
Descarga imágenes publicadas en Instagram.
Basada en https://youtu.be/nRiMZrQ3rpQ

DEPRECADO: Ahora IG te envía al login si intentas este tipo de request,
por lo cual este ejemplo está deprecado.

No lo elimino para poder observar y estudiar
el viejo método que se utilizaba para hacerlo.
"""

import requests
import re


def get_response(p_url):
    r = requests.get(p_url)
    while r.status_code != 200:
        # Utilizo recursividad para obtener una respuesta
        # hasta que funcione el request
        get_response(p_url)
    return r.text


def prepare_urls(matches):
    return list({match.replace("\\u0026", "") for match in matches})


url = input('Ingresa la url de Instragram: ')
response = get_response(url)

vid_matches = re.findall('"video_url":"([^"]+)"', response)
pic_matches = re.findall('"display_url":"([^"]+)"', response)

vid_urls = prepare_urls(vid_matches)
pic_urls = prepare_urls(pic_matches)

if vid_urls:
    print("Videos detectados:\n{0}".format('\n'.join(vid_urls)))

if pic_urls:
    print("Videos detectados:\n{0}".format('\n'.join(pic_urls)))

if not (vid_urls or pic_urls):
    print("No se encontraron imágenes o videos en la url")
