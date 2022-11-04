"""
Aplicación que genera notificaciones en el sistema operativo.
Basado en https://youtu.be/cfjPfYuZBZs
"""

from tkinter import *
from plyer import notification
from tkinter import messagebox


def create_notification():
    title = title_entry.get()
    msg = msg_entry.get()

    if title == "" or msg == "":
        messagebox.showerror("Atención", "Todos los campos son requeridos!")
        return

    notification.notify(title=title,
                        message=msg,
                        app_name=APP_NAME,
                        app_icon="icon.ico",
                        toast=True,
                        timeout=10)


root = Tk()
root.title('Notifier')
root.geometry("500x300")

header_image = PhotoImage(file="notify_label.png")
APP_NAME = "Notifier App"

Label(root, image=header_image).grid()

title_label = Label(root, text="Título de la notificación", font=("poppins", 10))
title_label.place(x=12, y=70)

title_entry = Entry(root, width=35, font=("poppins", 13))
title_entry.place(x=160, y=70)

# Label - Message
msg_label = Label(root, text="Descripción del Mensaje", font=("poppins", 10))
msg_label.place(x=12, y=120)

# ENTRY - Message
msg_entry = Entry(root, width=35, font=("poppins", 13))
msg_entry.place(x=160, height=100, y=120)

# Button
create_notification_btn = Button(root,
                                 text="Disparar Notificación",
                                 font=("poppins", 10, "bold"),
                                 fg="#ffffff",
                                 bg="#528DFF",
                                 width=20,
                                 relief="raised",
                                 command=create_notification)

create_notification_btn.place(x=170, y=230)

root.mainloop()
