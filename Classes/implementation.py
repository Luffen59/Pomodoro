
import tkinter as tk
from tkinter import messagebox
import pygame

class Implementation:
    @staticmethod
    def show_popup(title, message):
        root = tk.Tk()
        root.title(title)
        label = tk.Label(root, text=message)
        label.pack(padx=30, pady=40)
        root.after(1800, root.destroy)
        root.mainloop()

    @staticmethod
    def play_sound(sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()