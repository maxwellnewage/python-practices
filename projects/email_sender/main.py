"""
Envío de emails mediante gmail
https://www.youtube.com/watch?v=g_j6ILT-X0k
"""

import smtplib
import ssl
from decouple import config
from email.message import EmailMessage


# armo el mensaje del email
email_message = EmailMessage()
email_message['From'] = config('SENDER_EMAIL')
email_message['To'] = config('RECIEVER_EMAIL')
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
        config('SENDER_EMAIL'),
        config('SENDER_TOKEN')
    )
    # envío el email
    server.sendmail(
        config('SENDER_EMAIL'),
        config('RECIEVER_EMAIL'),
        email_message.as_string()
    )

print("email enviado!")
