"""
Buscador de anime que se conecta con la API Jikan
"""

import requests


def search_anime_by_term(term):
    return requests.request(
        "GET",
        "https://api.jikan.moe/v4/anime/",
        headers={
            'X-RapidAPI-Key': 'OLvXmpBtu5DA3lKXE7Lg9iHoIr9xO3nO',
            'X-RapidAPI-Host': 'jikan1.p.rapidapi.com'
        },
        params={'q': term}
    ).json()


if __name__ == '__main__':
    print("--------------------------------------------")
    print("Bienvenido a Anime Finder!")
    input_term = input("Dime que anime quieres buscar: ")
    print("Buscando...")
    print("--------------------------------------------")

    anime_list: list = search_anime_by_term(input_term)['data']
    if not anime_list:
        print("No se encontraron resultados :(")
    else:
        for anime in anime_list:
            print("Animes encontrados:")
            print("Títulos del anime")
            for item in anime['titles']:
                print(f"Idioma {item['type']}: {item['title']}")
            print(f"Tipo: {anime['type']}")
            print(f"Episodios: {anime['episodes']}")
            print(f"Estado Actual: {anime['status']}")
            print(f"Duración: {anime['duration']}")
            print(f"Rating: {anime['rating']}")
            print(f"Score: {anime['score']}")
            print(f"Popularidad: {anime['popularity']}")
            season = anime['season'] \
                if anime['season'] is not None \
                else 'No existe información'
            print(f"Temporada: {season}")

            year = anime['year'] \
                if anime['year'] is not None \
                else 'No existe información'
            print(f"Año: {year}")
            print("---------------------------------")
