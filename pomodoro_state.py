class PomodoroState:
    def __init__(self):
        self.work_period = True  # Initial state, assuming the Pomodoro timer starts with work

    def switch_to_break(self):
        self.work_period = False

    def switch_to_work(self):
        self.work_period = True

    def is_work_time(self):
        return self.work_period
