
import tkinter as tk
from tkinter import messagebox
import pygame
import time

class Implementation:
    @staticmethod
    def show_popup(title, message, duration=1):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title, message)
        root.after(duration, root.destroy())

    @staticmethod
    def play_sound(sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()