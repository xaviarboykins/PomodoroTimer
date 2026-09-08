"""Debug and write code: Write a standalone function validate_positive_int(value, name) that raises a useful
ValueError unless the value is a positive integer. Reject True and False too. Explain how your function handles
3, 0, "3", None, and True, and why your current validation encounters TypeError for some of these inputs."""
from config import TimerSettings
from pomodoro import PomodoroTimer


def validate_positive_int(value: int, name: str):
    if type(value) is not int or value < 1:
        raise ValueError(f"{name} must be a positive integer.")

"""
first the function warns with the annotation, then the function raises a ValueError unless the value
is a positive integer. Then rejects True and False too by for not being the right type.
for 3 the program skips over both if's because it is a positive integer.
for 0 the program raises a ValueError because it is not a positive of negative integer its 0.
for the string "3" it raises a ValueError because it is not a positive integer it is a string.
for None the program raises a ValueError because it is not a positive integer it is type NONE.
for True the program raises a ValueError because it is not a positive integer it is a boolean.
"""

"""
Apply configuration: Using your existing classes, write a short snippet that creates two independent 
timers: one with defaults explicitly supplied, and another with 10-minute work sessions, 2-minute short breaks, 
8-minute long breaks, and a long break after three completed work sessions. Start both and show checks for their 
initial remaining_seconds. Explain why ticking one should not affect the other.
"""
# timer1 = PomodoroTimer(settings=TimerSettings(work_minutes=25,
#                                      short_break_minutes=5,
#                                      long_break_minutes=15,
#                                      work_sessions_before_long_break=4
#                                      )
#                        )
#
# timer2 = PomodoroTimer(settings=TimerSettings(work_minutes=10,
#                                      short_break_minutes=2,
#                                      long_break_minutes=8,
#                                      work_sessions_before_long_break=3
#                                      )
#                        )
#
# timer1.start()
# print(timer1.remaining_seconds)
#
# timer2.start()
# print(timer2.remaining_seconds)

settings = TimerSettings(work_minutes=7)
first = PomodoroTimer(settings)
settings.work_minutes = 9
second = PomodoroTimer(settings)

first.start()
print(first.settings.work_minutes)
print(first.remaining_seconds)
second.start()
print(second.settings.work_minutes)
print(second.remaining_seconds)