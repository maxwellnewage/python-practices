import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en el mismo directorio
load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
SENDER_TOKEN = os.getenv('SENDER_TOKEN')
