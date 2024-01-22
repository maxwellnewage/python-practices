"""
ISS Position App
"""
import requests

from email.message import EmailMessage
from level_intermediate import email
from projects.config.email_config import (
    SENDER_EMAIL,
    RECEIVER_EMAIL,
    SENDER_TOKEN
)


def send_email(lat, lng):
    email_message = EmailMessage()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = RECEIVER_EMAIL
    email_message['Subject'] = "Informe de Posición ISS"
    email_message.set_content(f"""
        Informe posicional.
        
        ISS está en la latitud {lat}, longitud {lng}
        """)

    email.send(
        SENDER_EMAIL,
        RECEIVER_EMAIL,
        SENDER_TOKEN,
        email_message
    )


if __name__ == '__main__':
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    send_email(latitude, longitude)
