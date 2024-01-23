"""
ISS Position App
"""
import requests

from level_intermediate import email


def send_email(lat, lng):
    msg_body = f"""
    Informe posicional.

    ISS está en la latitud {lat}, longitud {lng}
    """

    email_message = email.build_message(
        "Informe de Posición ISS",
        msg_body
    )

    email.send(email_message)


if __name__ == '__main__':
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    send_email(latitude, longitude)
