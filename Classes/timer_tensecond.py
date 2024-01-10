from Classes.timer import Timer

class TenSecondTimer(Timer):
    def __init__(self, work_duration, break_duration, message_printer, notification, pomodoro_state):
        super().__init__(work_duration, break_duration, message_printer, notification)
        self.pomodoro_state = pomodoro_state

    def do_work(self):
        if self.pomodoro_state.is_work_time():
            self.message_printer.print_work_message(self.work_duration)
        else:
            return

    def do_break(self):
        if self.pomodoro_state.is_work_time():
            self.message_printer.print_break_message(self.break_duration)
        else:
            return