import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en el mismo directorio
load_dotenv()

# email
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
SENDER_TOKEN = os.getenv('SENDER_TOKEN')

# https://home.openweathermap.org/api_keys
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# https://www.alphavantage.co/
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# https://newsapi.org/
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Chrome Binary Path
CHROMIUM_BINARY_PATH = os.getenv('CHROMIUM_BINARY_PATH')
