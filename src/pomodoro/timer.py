import helpers

class PomodoroTimer:
    def __init__(self,
                 schedule: tuple[str, ...],
                 work_time: int = 25,
                 short_break_time: int = 5,
                 long_break_time: int = 15) -> None:
        # Store the sequence of events
        self.session_schedule = schedule

        # Initialize session tracking data
        self.session_data: dict[str, dict[str, int]] = {
            "Work session": {"duration": helpers.minutes_to_seconds(work_time), "count": 0},
            "Short break": {"duration": helpers.minutes_to_seconds(short_break_time), "count": 0},
            "Long break": {"duration": helpers.minutes_to_seconds(long_break_time), "count": 0},
        }
        # Tracks current session
        self.current_session: str | None = None
        self.remaining_seconds: int = 0

    # Getters
    @property
    def formatted_time(self) -> str:
        return helpers.format_time(self.remaining_seconds)
    
    # Main Methods
    def reset(self) -> None:
        print(f"Resetting Pomodoro Timer...")
        self.current_session = None
        for data in self.session_data.values():
            data["count"] = 0
        self.remaining_seconds = 0
        print(f"Pomodoro Timer has been reset")