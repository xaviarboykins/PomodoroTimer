import pytest
from pomodoro.type_definitions import SessionType
from pomodoro.timer import PomodoroTimer

@pytest.fixture
def pomodoro_timer():
    return PomodoroTimer()

def test_pomodoro_timer_start(pomodoro_timer: PomodoroTimer):
    pomodoro_timer.start()
    assert pomodoro_timer.state == SessionType.WORK, "initial session state should be work"
    assert pomodoro_timer.remaining_seconds == 1500, "remaining_seconds should be 1500"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

def test_pomodoro_timer_complete_session(pomodoro_timer: PomodoroTimer):
    pomodoro_timer.start()
    pomodoro_timer.complete_session()
    assert pomodoro_timer.state == SessionType.SHORT_BREAK, "state should be short break"
    assert pomodoro_timer.remaining_seconds == 300, "remaining_seconds should be 300"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.completed_work_sessions == 1, "completed_work_sessions should be 1"

def test_pomodoro_timer_reset(pomodoro_timer: PomodoroTimer):
    pomodoro_timer.start()
    pomodoro_timer.complete_session()
    pomodoro_timer.start()
    pomodoro_timer.complete_session()
    pomodoro_timer.start()
    pomodoro_timer.complete_session()
    assert pomodoro_timer.state == SessionType.SHORT_BREAK, "state should be short break"
    assert pomodoro_timer.remaining_seconds == 300, "remaining_seconds should be 300"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.completed_work_sessions == 2, "completed_work_sessions should be 2"

    pomodoro_timer.reset()
    assert pomodoro_timer.state == SessionType.IDLE, "initial state should be idle"
    assert pomodoro_timer.remaining_seconds == 0, "remaining_seconds should be 0"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"
