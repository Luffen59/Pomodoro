import time
class Countdown:
    def __init__(self, work_duration, break_duration, message_printer):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.message_printer = message_printer

    def run(self):
        while True:
            self.message_printer.print_work_message(self.work_duration)
            time.sleep(self.work_duration)

            self.message_printer.print_break_message(self.break_duration)
            time.sleep(self.break_duration)
