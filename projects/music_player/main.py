"""
Reproductor de música.
Basado en https://youtu.be/SCos1o368iE

Dejé un archivo en resources/Luke_Bryan_Country_On.mp3 para testear el reproductor,
pero se puede utilizar también con archivos de tu propia PC.
"""

from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title("Maxwell Music Player")
root.geometry("500x300")

pygame.mixer.init()

menu_bar = Menu(root)
root.config(menu=menu_bar)

songs = []
current_song = ""
paused = False


def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)

        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        song_list.insert("end", song)

    song_list.select_set(0)
    current_song = songs[song_list.curselection()[0]]


def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()
        paused = False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_music():
    global current_song, paused

    try:
        song_list.selection_clear(0, END)
        song_list.selection_set(songs.index(current_song) + 1)
        current_song = songs[song_list.curselection()[0]]
        play_music()
    except:
        pass


def previous_music():
    global current_song, paused
    try:
        song_list.selection_clear(0, END)
        song_list.selection_set(songs.index(current_song) - 1)
        current_song = songs[song_list.curselection()[0]]
        play_music()
    except:
        pass


open_menu = Menu(menu_bar, tearoff=False)
open_menu.add_command(label='Seleccionar Carpeta', command=load_music)
menu_bar.add_cascade(label='Seleccionar', menu=open_menu)

song_list = Listbox(root, bg="black", fg="white", width=100, height=15)
song_list.pack()

play_btn_image = PhotoImage(file='resources/play.png')
pause_btn_image = PhotoImage(file='resources/pause.png')
next_btn_image = PhotoImage(file='resources/next.png')
previous_btn_image = PhotoImage(file='resources/previous.png')

control_frame = Frame(root)
control_frame.pack()

# Me quería llevar esto a objetos, pero no puedo pasar parámetros a las funciones de command
play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=0, command=previous_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()
