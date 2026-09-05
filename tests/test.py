from session_types import SessionType
from timer import PomodoroTimer

configured_session_times:list[int] = [1, 1, 1]

timer = PomodoroTimer(work_time=configured_session_times[0],
                      short_break_time=configured_session_times[1],
                      long_break_time=configured_session_times[2])

timer.start()
print(timer.state.name)
print(f"is paused: {timer.is_paused}")
print(f"Seconds left: {timer.remaining_seconds}")
print(f"Completed work sessions: {timer.completed_work_sessions}")

assert timer.state == SessionType.WORK
assert timer.is_paused is False
assert timer.remaining_seconds == 60
assert timer.completed_work_sessions == 0

timer.complete_session()
timer.complete_session()
timer.complete_session()
timer.complete_session()
timer.complete_session()
timer.complete_session()
timer.complete_session()

print(timer.state.name)
print(f"is paused: {timer.is_paused}")
print(f"Seconds left: {timer.remaining_seconds}")
print(f"Completed work sessions: {timer.completed_work_sessions}")

assert timer.state == SessionType.LONG_BREAK
assert timer.is_paused is False
assert timer.remaining_seconds == 60
assert timer.completed_work_sessions == 4
