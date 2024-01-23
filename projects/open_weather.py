import requests
import geocoder

from projects.config.globals import WEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_by_city(city):
    response = requests.get(BASE_URL, params={
        "q": city,
        "appid": WEATHER_API_KEY
    })
    print(response.json())


def get_by_location(lat, lng):
    response = requests.get(BASE_URL, params={
        "lat": lat,
        "lon": lng,
        "appid": WEATHER_API_KEY
    })
    print(response.json())


def get_location():
    location = geocoder.ip('me')

    if location.ok:
        return location.latlng[0], location.latlng[1]


if __name__ == '__main__':
    get_by_city("BuenosAires")
    get_by_location(*get_location())
