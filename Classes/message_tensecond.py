
from Classes.notification import Notification  # Import the Notification class
from Classes.message import Message

class TenSecondMessage(Message):

    def print_work_message(self, duration):
        print("Work")
        self.notification.show_popup("", "It's time to work!")
        self.notification.play_sound("path/file.mp3")


    def print_break_message(self, duration):
        print("Take a 10 seconds break")
        self.notification.show_popup("", "Take a 10 seconds break!")
        self.notification.play_sound("path/file.mp3")
