import time
from abc import ABC, abstractmethod
from Classes.notification import Notification

class Timer:
    def __init__(self, work_duration, break_duration, message_printer, notification):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.message_printer = message_printer
        self.notification = notification

    def run(self):
        while True:
            self.do_work()
            time.sleep(self.work_duration)

            self.do_break()
            time.sleep(self.break_duration)

    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def do_break(self):
        pass