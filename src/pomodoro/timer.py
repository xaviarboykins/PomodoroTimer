import helpers
from session_types import SessionType

class PomodoroTimer:
    def __init__(self, work_time: int = 25,
                 short_break_time: int = 5,
                 long_break_time: int = 15) -> None:
        """ Pomodoro Timer STATE MACHINE """
        # Session
        # Initialize session tracking data
        self.session_data: dict[str, dict[str, int]] = {
            "WORK": {"duration": work_time},
            "SHORT_BREAK": {"duration": short_break_time},
            "LONG_BREAK": {"duration": long_break_time},
        }

        self.completed_work_sessions = 0

        # Timer
        self.state: SessionType = SessionType.IDLE
        self.remaining_seconds: int = 0
        self.is_paused = False

    # Getters
    @property
    def formatted_time(self) -> str:
        return helpers.format_time(self.remaining_seconds)

    def get_duration(self, session_type: SessionType) -> int:
        return self.session_data[session_type.name]["duration"]

    # Setters
    def set_remaining_secs(self, time_in_minutes: int) -> None:
        self.remaining_seconds = helpers.minutes_to_seconds(time_in_minutes)

    # Main Methods
    def start(self) -> None:
        # Initializes first Work session
        if self.state == SessionType.IDLE:
            self._set_session(SessionType.WORK)

        self.is_paused = False

        # HERE WE MAY Begin countdown of current session later

    def pause(self) -> None:
        self.is_paused = True

    def resume(self) -> None:
        self.is_paused = False

    def reset(self) -> None:
        """resets Pomodoro Timer and manager state completely """
        # reset manager values
        self.state = SessionType.IDLE
        self.completed_work_sessions = 0

        # reset Pomodoro Timer
        self.remaining_seconds = 0
        self.is_paused = False

    def skip(self) -> None:
        self._advance_session()

    def complete_session(self) -> None:
        """Completes Session and increases work session count if a work session was completed"""
        if self.state == SessionType.WORK:
            self.completed_work_sessions += 1

        self._advance_session()

    # Local Helpers
    def _advance_session(self) -> None:
        """Controls session transition and decides what session should come next"""
        if self.state == SessionType.WORK:
            # Every 4th completed work session leads to a long break
            if self.completed_work_sessions > 0 and self.completed_work_sessions % 4 == 0:
                self._set_session(SessionType.LONG_BREAK)
            else:
                self._set_session(SessionType.SHORT_BREAK)
        elif self.state in [SessionType.SHORT_BREAK, SessionType.LONG_BREAK]:
            self._set_session(SessionType.WORK)


    def _set_session(self, session_type: SessionType) -> None:
        self.state = session_type

        duration = self.get_duration(session_type)
        self.set_remaining_secs(duration)

        self.is_paused = False