"""
Envío de emails mediante gmail
https://www.youtube.com/watch?v=g_j6ILT-X0k
"""

import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

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

context = ssl.create_default_context()

# creo una instancia de una conexión SMTP en gmail
print("conectando...")
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    # me autentico
    server.login(
        SENDER_EMAIL,
        SENDER_TOKEN
    )
    # envío el email
    server.sendmail(
        SENDER_EMAIL,
        RECEIVER_EMAIL,
        email_message.as_string()
    )

print("email enviado!")
