import time
from abc import ABC, abstractmethod

class Message:
    def __init__(self, notification):
        self.notification = notification

    @abstractmethod
    def print_work_message(self, duration):
        pass

    @abstractmethod
    def print_break_message(self, duration):
        pass