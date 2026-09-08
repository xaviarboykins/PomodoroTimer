import pytest
from pomodoro.config import TimerSettings
from pomodoro.type_definitions import SessionType
from pomodoro.timer import PomodoroTimer

@pytest.fixture
def pomodoro_timer():
    return PomodoroTimer()

def test_timer_valid_settings(pomodoro_timer: PomodoroTimer):
    """Tests that the timer has valid default settings from JSON"""
    timer = PomodoroTimer()
    assert timer.settings == TimerSettings(25,5,15,4)

def test_timer_invalid_settings(pomodoro_timer: PomodoroTimer):
    """Tests that invalid timer settings raise ValueError."""

    with pytest.raises(ValueError, match=".*must be an int greater than 0.*"): # Negative time for work
        pomodoro_timer.settings = TimerSettings(-1,5,10,4)

    with pytest.raises(ValueError, match=".*must be an int greater than 0.*"): # Zero time for short break
        pomodoro_timer.settings = TimerSettings(25,0,15,4)

    with pytest.raises(ValueError, match=".*must be an int greater than 0."): # Negative time for long break
        pomodoro_timer.settings = TimerSettings(25,5,-1,4)

    with pytest.raises(ValueError, match=".*must be an int greater than 0."): # no work requirement for long breaks
        pomodoro_timer.settings = TimerSettings(25,5,15,0)

def test_pomodoro_timer_start(pomodoro_timer: PomodoroTimer):
    """Tests that the pomodoro timer starts correctly and completes a session"""
    pomodoro_timer.start() # starts session
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1500, "remaining_seconds should be 1500"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == True, "session_in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

def test_pomodoro_timer_pause_resume(pomodoro_timer: PomodoroTimer):
    """Tests that the pomodoro timer pauses and remaining time is unaffected by tick"""
    pomodoro_timer.start() ## starts a work session
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1500, "remaining_seconds should be 1500"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == True, "session_in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

    pomodoro_timer.tick() # progresses work session by 1 sec
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1499, "remaining_seconds should be 1499"
    assert pomodoro_timer.is_paused == False, "is_paused should be True"
    assert pomodoro_timer.session_in_progress == True, "in_progress should be True"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

    pomodoro_timer.pause() # pauses session
    # test that tick doesn't progress timer
    pomodoro_timer.tick()
    pomodoro_timer.tick()
    pomodoro_timer.tick()
    pomodoro_timer.tick()
    pomodoro_timer.tick()
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1499, "remaining_seconds should be 1499"
    assert pomodoro_timer.is_paused == True, "is_paused should be True"
    assert pomodoro_timer.session_in_progress == True, "in_progress should be True"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

    pomodoro_timer.resume() # resumes session this should call start again automaticly
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1499, "remaining_seconds should be 1499"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == True, "in_progress should be True"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

    pomodoro_timer.tick() # progresses work session by 1 sec
    assert pomodoro_timer.state == SessionType.WORK, "session state should be work"
    assert pomodoro_timer.remaining_seconds == 1498, "remaining_seconds should be 1498"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == True, "in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 0, "completed_work_sessions should be 0"

    # completes the full session which should be a work session and should set up the next session
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()
    assert pomodoro_timer.state == SessionType.SHORT_BREAK, "session state should be short break"
    assert pomodoro_timer.remaining_seconds == 300, "remaining_seconds should be 300"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == False, "in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 1, "completed_work_sessions should be 0"

    pomodoro_timer.tick() # test that tick doesn't progress timer because session hasn't started
    assert pomodoro_timer.state == SessionType.SHORT_BREAK, "session state should be short break"
    assert pomodoro_timer.remaining_seconds == 300, "remaining_seconds should be 300"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == False, "in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 1, "completed_work_sessions should be 0"

    # starts short break session to verify that a tick actually accounts that the session is in progress
    pomodoro_timer.start()
    pomodoro_timer.tick()
    assert pomodoro_timer.state == SessionType.SHORT_BREAK, "session state should be short break"
    assert pomodoro_timer.remaining_seconds == 299, "remaining_seconds should be 299"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == True, "in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 1, "completed_work_sessions should be 0"

def test_fourth_work_session(pomodoro_timer):
    pomodoro_timer.start() # WORK 1
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Short Break
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Work 2
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Short Break
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Work 3
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Short Break
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    pomodoro_timer.start() # Work 4 this should earn a long break
    for _ in range(pomodoro_timer.remaining_seconds):
        pomodoro_timer.tick()

    assert pomodoro_timer.state == SessionType.LONG_BREAK, "session state should be long break"
    assert pomodoro_timer.remaining_seconds == 900, "remaining_seconds should be 900"
    assert pomodoro_timer.is_paused == False, "is_paused should be False"
    assert pomodoro_timer.session_in_progress == False, "in_progress should be False"
    assert pomodoro_timer.completed_work_sessions == 4, "completed_work_sessions should be 0"
