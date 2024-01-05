from message import Message

class TenSecondMessage(Message):
    def print_work_message(self, duration):
        print(f"Work")

    def print_break_message(self, duration):
        print(f"Take a 10 seconds break")