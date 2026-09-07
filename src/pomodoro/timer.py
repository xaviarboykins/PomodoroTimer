from pomodoro.type_definitions import SessionType
from pomodoro.utils import format_time, minutes_to_seconds
from pomodoro.session import get_next_session


class PomodoroTimer:
    """Pomodoro Timer:
    Manages Manages the Pomodoro session lifecycle, including IDLE, WORK, SHORT_BREAK,
    and LONG_BREAK states.
    Tracks completed work sessions, the current session, and how many seconds are left
    in the session.
    Controls starting sessions and transitions between work and break sessions based on the rule: every four
    completed WORK sessions earns a LONG_BREAK, otherwise results in a SHORT_BREAK session.
    """
    def __init__(self, work_time: int = 25,
                 short_break_time: int = 5,
                 long_break_time: int = 15) -> None:
        # Sessions
        # Initialize session tracking data
        self.session_data: dict[str, dict[str, int]] = {
            "WORK": {"duration": work_time},
            "SHORT_BREAK": {"duration": short_break_time},
            "LONG_BREAK": {"duration": long_break_time},
        }
        self.state: SessionType = SessionType.IDLE

        # Tracks complete
        self.completed_work_sessions = 0

        # Timer
        self.remaining_seconds: int = 0
        self.is_paused = False
        self.session_in_progress = False

    # Getters
    @property
    def formatted_time(self) -> str:
        """Returns a formatted string: MM:SS based on remaining_seconds"""
        return format_time(self.remaining_seconds)

    def get_duration(self, session_type: SessionType) -> int:
        """Gets current session duration in minutes"""
        return self.session_data[session_type.name]["duration"]

    # Setters
    def set_remaining_secs(self, time_in_minutes: int) -> None:
        """Sets remaining session duration in seconds"""
        self.remaining_seconds = minutes_to_seconds(time_in_minutes)

    # Main Methods
    def start(self) -> None:
        """Starts Pomodoro Timer session"""
        # Initializes first Work session
        if self.state == SessionType.IDLE:
            self._set_session(SessionType.WORK)

        self.session_in_progress = True

        # progress session


    def pause(self) -> None:
        """Pauses Pomodoro Timer session sets is_paused to True"""
        self.is_paused = True

    def resume(self) -> None:
        """Resumes Pomodoro Timer session: sets is_paused to False"""
        self.is_paused = False
        self.start()

    def reset(self) -> None:
        """Resets Pomodoro Timer state completely and set state to IDLE"""
        # reset manager values
        self.state = SessionType.IDLE
        self.completed_work_sessions = 0

        # reset Pomodoro Timer
        self.remaining_seconds = 0
        self.is_paused = False
        self.session_in_progress = False

    def tick(self) -> None:
        if self.remaining_seconds > 0 and not self.is_paused and self.session_in_progress:
            self.remaining_seconds -= 1
            if self.remaining_seconds == 0:
                self.complete_session()


    def skip(self) -> None:
        """Skips current Pomodoro Timer session and advances to the next session"""
        self._advance_session()

    def complete_session(self) -> None:
        """Completes Session and increases work session count if a work session was completed"""
        if self.state == SessionType.WORK:
            self.completed_work_sessions += 1
        self._advance_session()

    # Local Helpers
    def _advance_session(self) -> None:
        """Advances the timer to the next Pomodoro session."""
        next_session = get_next_session(
            self.state,
            self.completed_work_sessions
        )

        self._set_session(next_session)
        self.session_in_progress = False


    def _set_session(self, session_type: SessionType) -> None:
        """Sets new session state to WORK, SHORT_BREAK, or LONG_BREAK,
        loads session configured duration into remaining_seconds and clears paused flag
        """
        self.state = session_type

        duration = self.get_duration(session_type)
        self.set_remaining_secs(duration)

        self.is_paused = False