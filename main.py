from pomodoro_message import Pomodoro_message
from tensecond_message import Ten_second_message
from countdown import Countdown
import time
import random
import threading

if __name__ == "__main__":

    pomodoro = Countdown(25 * 60, 5 * 60, Pomodoro_message())
    ten_seconds = Countdown(random.randint(90, 150), 12, Ten_second_message())

    pomodoro = threading.Thread(target=pomodoro.run)
    ten_seconds = threading.Thread(target=ten_seconds.run)

    pomodoro.start()
    ten_seconds.start()

    pomodoro.join()
    ten_seconds.join()