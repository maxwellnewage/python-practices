"""
Envío de emails mediante gmail
https://www.youtube.com/watch?v=g_j6ILT-X0k
"""


from email.message import EmailMessage
from level_intermediate import email
from projects.config.email_config import SENDER_EMAIL, RECEIVER_EMAIL, SENDER_TOKEN

if __name__ == '__main__':
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

    email.send(
        SENDER_EMAIL,
        RECEIVER_EMAIL,
        SENDER_TOKEN,
        email_message
    )
