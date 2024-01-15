
from Classes.notification import Notification  # Import the Notification class
from Classes.message import Message

class TenSecondMessage(Message):

    def print_work_message(self, duration):
        print("Work TS")
        self.notification.show_popup("", "Keep going!")
        self.notification.play_sound("/home/lucas/Documents/Pomodoro/Sound/musical-guitar-string.wav")
        # "path/file.mp3"

    def print_break_message(self, duration):
        print("Break TS")
        self.notification.show_popup("", "Breath")
        self.notification.play_sound("/home/lucas/Documents/Pomodoro/Sound/guitar-string-tone.wav")   # "path/file.mp3"
