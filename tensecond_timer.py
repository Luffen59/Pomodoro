from timer import Timer
from pomodoro_timer import PomodoroTimer
import threading
import time


class TenSecondTimer(Timer):
    def __init__(self, work_duration, break_duration, message_printer, run_flag):
        super().__init__(work_duration, break_duration, message_printer)
        self.run_flag = run_flag

    def flag_management(self):
        pomodoro_instance = PomodoroTimer(self.work_duration, self.break_duration, self.message_printer)
        while True:
            if self.run_flag:
                pomodoro_instance.do_work()
                self.run_flag = True
            elif not self.run_flag:
                pomodoro_instance.do_break()
                self.run_flag = False

    def run(self):
        while True:
            if self.run_flag:
                run(self)
                super().run()
            elif not self.run_flag:
                return

#    def run(self):
#        while self.run_flag:
#            super().run()