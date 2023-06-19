"""
Detecta que tan rápido escribes.
Basado en https://www.youtube.com/watch?v=quBb--IJPPc&ab_channel=NeuralNine

CPS = Characters Per Second - Caracteres por segundo
CPM = Characters Per Minute - Caracteres por minuto
WPS = Words Per Second - Palabras por segundo
WPM = Words Per Minute - Palabras por minuto
"""

import tkinter as tk
import time
import threading
import random


class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")
        self.text_type_list = [
            "Hola mundo.",
            "El mundo necesita mas desarrolladores.",
            "Esto es una prueba de escritura para medir tu velocidad."
        ]

        self.SPEED_LABEL_DEFAULT_TEXT = \
            "Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM"

        self.string_var_sl = tk.StringVar(value=self.SPEED_LABEL_DEFAULT_TEXT)

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(
            self.frame,
            text=random.choice(self.text_type_list),
            font=("Helvetica", 18)
        )

        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(
            self.frame,
            width=40,
            font=("Helvetica", 24)
        )

        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(
            self.frame,
            font=("Helvetica", 18),
            textvariable=self.string_var_sl
        )

        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(
            self.frame,
            text="Reset",
            command=self.reset
        )

        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        sample_label_text = self.sample_label.cget('text')

        if not self.running:
            # verificamos si no esta apretando la tecla shift o control
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not sample_label_text.startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == sample_label_text[:-1]:
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split()) / self.counter
            wpm = wps * 60

            self.string_var_sl.set(
                f"Speed:\n"
                f"{cps:.2f} CPS\n"
                f"{cpm:.2f} CPM\n"
                f"{wps:.2f} WPS\n"
                f"{wpm:.2f} WPM"
            )

    def reset(self):
        self.running = False
        self.counter = 0
        self.string_var_sl.set(self.SPEED_LABEL_DEFAULT_TEXT)
        self.sample_label.config(text=random.choice(self.text_type_list))
        self.input_entry.delete(0, tk.END)


TypeSpeedGUI()
