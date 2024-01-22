"""
Send email function
"""

import smtplib
import ssl


def send(sender, receiver, token, msg):
    context = ssl.create_default_context()

    # creo una instancia de una conexión SMTP en gmail
    print("conectando...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        # me autentico
        server.login(
            sender,
            token
        )
        # envío el email
        server.sendmail(
            sender,
            receiver,
            msg.as_string()
        )

    print("email enviado!")