from session_types import SessionType
from timer import PomodoroTimer


if __name__ == "__main__":
    configured_session_times:list[int] = [1, 1, 1]

    timer = PomodoroTimer(work_time=configured_session_times[0],
                          short_break_time=configured_session_times[1],
                          long_break_time=configured_session_times[2])
