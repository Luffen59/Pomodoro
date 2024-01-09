from Classes.timer import Timer

class PomodoroTimer(Timer):
    def __init__(self, work_duration, break_duration, message_printer, pomodoro_state):
        super().__init__(work_duration, break_duration, message_printer)
        self.pomodoro_state = pomodoro_state

    def do_work(self):
        # Perform work-related tasks
        self.message_printer.print_work_message(self.work_duration)
        # After work, switch to break
        self.pomodoro_state.switch_to_work()

    def do_break(self):
        # Perform break-related tasks
        self.message_printer.print_break_message(self.break_duration)
        # After break, switch back to work
        self.pomodoro_state.switch_to_break()
