"""
Devuelve un artículo aleatorio de Wikipedia.
Basado en https://youtu.be/ViXs3wEJ1UY
"""
import webbrowser

import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Special:Random"

article_page = requests.get(url)

soup = BeautifulSoup(article_page.text, "html.parser")
article_title = soup.find(id='firstHeading')

print(f"El título del artículo aleatorio es: {article_title.string}")

read = input("Quieres ver el artículo? (s/n): ")
if read == 's':
    webbrowser.open(article_page.url)

print(f"La URL es: {article_page.url}")
