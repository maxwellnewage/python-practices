"""
Envío de emails mediante gmail
https://www.youtube.com/watch?v=g_j6ILT-X0k
"""

from level_intermediate import email

if __name__ == '__main__':
    email_message = email.build_message(
        "hola!",
        """
            Hola Maxi!

            Como estas? :D


            Saludos!
        """
    )

    email.send(email_message)
