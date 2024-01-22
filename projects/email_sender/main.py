"""
Envío de emails mediante gmail
https://www.youtube.com/watch?v=g_j6ILT-X0k
"""


import os
from email.message import EmailMessage
from dotenv import load_dotenv
from level_intermediate import email


if __name__ == '__main__':
    # Cargar variables de entorno desde el archivo .env en el mismo directorio
    load_dotenv()

    # constantes
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
    SENDER_TOKEN = os.getenv('SENDER_TOKEN')

    # armo el mensaje del email
    email_message = EmailMessage()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = RECEIVER_EMAIL
    email_message['Subject'] = "hola!"
    email_message.set_content("""
    Hola Maxi!

    Como estas? :D


    Saludos!
    """)

    email.send(SENDER_EMAIL, RECEIVER_EMAIL, SENDER_TOKEN, email_message)
