

class RunFlag:
    def __init__(self, flag):
        self.flag = flag

    def flag_management(self):
        pomodoro_instance = PomodoroTimer(self.work_duration, self.break_duration, self.message_printer)
        while True:
            if self.flag:
                pomodoro_instance.do_work()
                self.flag = True
            elif not self.flag:
                pomodoro_instance.do_break()
                self.flag = False