from pomodoro_message import PomodoroMessage
from tensecond_message import TenSecondMessage
from pomodoro_timer import PomodoroTimer
from tensecond_timer import TenSecondTimer
import time
import random
import threading


if __name__ == "__main__":
    run_flag = threading.Event()  # Create an event object

    pomodoro = PomodoroTimer(25, 5, PomodoroMessage())
    ten_seconds = TenSecondTimer(random.randint(3, 3), 1, TenSecondMessage(), run_flag)

    pomodoro_thread = threading.Thread(target=pomodoro.run)
    ten_seconds_thread = threading.Thread(target=ten_seconds.run)
    ten_seconds_thread_flag = threading.Thread(target=ten_seconds.flag_management)

    pomodoro_thread.start()
    ten_seconds_thread.start()
    ten_seconds_thread_flag.start()

    pomodoro_thread.join()
    ten_seconds_thread.join()

