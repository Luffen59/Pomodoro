from Classes.message_pomodoro import PomodoroMessage
from Classes.message_tensecond import TenSecondMessage
from Classes.timer_pomodoro import PomodoroTimer
from Classes.timer_tensecond import TenSecondTimer
from Classes.state_pomodoro import PomodoroState
from Classes.notification import Notification
from Classes.find_OS import OSFinder

import random
import threading

if __name__ == "__main__":
    pomodoro_state = PomodoroState()

    implementation = OSFinder().get_platform_implementation()

    notification = Notification(implementation)

    pomodoro = PomodoroTimer(25, 5, PomodoroMessage(notification), notification,
                             pomodoro_state)
    ten_seconds = TenSecondTimer(random.randint(3, 4), 1, TenSecondMessage(notification),
                                 notification, pomodoro_state)

    pomodoro_thread = threading.Thread(target=pomodoro.run)
    ten_seconds_thread = threading.Thread(target=ten_seconds.run)

    pomodoro_thread.start()
    ten_seconds_thread.start()

    pomodoro_thread.join()
    ten_seconds_thread.join()
