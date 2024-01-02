from message import Message

class Pomodoro_message(Message):
    def print_work_message(self, duration):
        print(f"Work for {duration // 60} minutes")

    def print_break_message(self, duration):
        print(f"Take a {duration // 60} minute break")