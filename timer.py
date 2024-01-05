import time
class Timer:
    def __init__(self, work_duration, break_duration, message_printer):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.message_printer = message_printer

    def run(self):
        while True:
            self.do_work()
            time.sleep(self.work_duration)

            self.do_break()
            time.sleep(self.break_duration)

    def do_work(self):
        self.message_printer.print_work_message(self.work_duration)

    def do_break(self):
        self.message_printer.print_break_message(self.break_duration)
