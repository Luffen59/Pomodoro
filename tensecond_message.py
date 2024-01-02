from message import Message

class Ten_second_message(Message):
    def print_work_message(self, duration):
        print(f"Work")

    def print_break_message(self, duration):
        print(f"Take a 10 seconds break")