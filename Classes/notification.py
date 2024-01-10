from Classes.implementation import Implementation

class Notification:
    def __init__(self, implementation):
        self.implementation = implementation

    def show_popup(self, title, message):
        self.implementation.show_popup(title, message)

    def play_sound(self, sound_file):
        self.implementation.play_sound(sound_file)