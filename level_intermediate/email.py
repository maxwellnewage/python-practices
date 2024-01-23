"""
Send email function
"""

import smtplib
import ssl
from email.message import EmailMessage
from projects.config.globals import (
    SENDER_EMAIL,
    RECEIVER_EMAIL,
    SENDER_TOKEN
)


def build_message(subject, message):
    email_message = EmailMessage()
    email_message['From'] = SENDER_EMAIL
    email_message['To'] = RECEIVER_EMAIL
    email_message['Subject'] = subject
    email_message.set_content(message)

    return email_message


def send(msg):
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
            msg.as_string()
        )

    print("email enviado!")
