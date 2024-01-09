from pomodoro_message import PomodoroMessage
from tensecond_message import TenSecondMessage
from pomodoro_timer import PomodoroTimer
from tensecond_timer import TenSecondTimer
from pomodoro_state import PomodoroState
import time
import random
import threading

if __name__ == "__main__":
    pomodoro_state = PomodoroState()

    pomodoro = PomodoroTimer(25, 5, PomodoroMessage(), pomodoro_state)
    ten_seconds = TenSecondTimer(random.randint(3, 4), 1, TenSecondMessage(), pomodoro_state)

    pomodoro_thread = threading.Thread(target=pomodoro.run)
    ten_seconds_thread = threading.Thread(target=ten_seconds.run)

    pomodoro_thread.start()
    ten_seconds_thread.start()

    pomodoro_thread.join()
    ten_seconds_thread.join()
