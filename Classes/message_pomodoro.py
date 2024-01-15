
from Classes.notification import Notification  # Import the Notification class
from Classes.message import Message

class PomodoroMessage(Message):

    def print_work_message(self, duration):
        print("Work Pomodoro")
        self.notification.show_popup("", f"Work for {duration // 60} minutes")
        self.notification.play_sound("path/file.mp3")

    def print_break_message(self, duration):
        print("Break Pomodoro")
        self.notification.show_popup("", f"Take a {duration // 60} minute break")
        self.notification.play_sound("path/file.mp3")


