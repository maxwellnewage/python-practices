"""
Descarga videos desde YouTube.
Basado en https://youtu.be/86U1b21qwhs
"""
import threading

from pytube import YouTube
from tkinter import Button, Entry, Label, Menu, Frame, StringVar, Tk

INSTRUCTIONS_DEFAULT_TEXT = \
    "Escribe un link y presiona descargar para empezar!"
INSTRUCTIONS_PROGRESS_TEXT = "Descargando..."
INSTRUCTIONS_DONE_TEXT = "Tu video ha sido descargado!"


def download():
    string_var_instructions.set(INSTRUCTIONS_PROGRESS_TEXT)
    t = threading.Thread(target=async_download)
    t.start()


def async_download():
    video = YouTube(video_url.get())
    download_video = video.streams.get_highest_resolution()
    download_video.download()
    string_var_instructions.set(INSTRUCTIONS_DONE_TEXT)


root = Tk()
root.geometry("500x300")
root.title("YouTube Video Downloader")

string_var_instructions = StringVar(value=INSTRUCTIONS_DEFAULT_TEXT)

frame = Frame(root)

# Menú superior
menu_bar = Menu(root)
root.config(menu=menu_bar)
menu_bar.add_command(label='Salir', command=root.destroy)

# Título
title_label = Label(
    frame,
    text="YouTube Video Downloader",
    font=("Helvetica", 18)
)
title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# Instrucciones
instructions_label = Label(
    frame,
    textvariable=string_var_instructions,
    font=("Helvetica", 14)
)
instructions_label.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

# Campo de URL
video_url = Entry(frame, width=40)
video_url.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Botón de descarga
download_btn = Button(frame, text="Descargar", command=download)
download_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

frame.pack(expand=True)

root.mainloop()
