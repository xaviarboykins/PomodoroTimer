from dataclasses import dataclass
import json
from pathlib import Path


@dataclass
class TimerSettings:
    work_minutes: int = 25
    short_break_minutes: int = 5
    long_break_minutes: int = 15
    work_sessions_before_long_break: int = 4

    def __post_init__(self):
        if type(self.work_minutes) is not int or self.work_minutes <= 0 :
            raise ValueError("work time must be an int greater than 0.")
        if type(self.short_break_minutes) is not int or self.short_break_minutes <= 0:
            raise ValueError("short break time must be an int greater than 0.")
        if type(self.long_break_minutes) is not int or self.long_break_minutes <= 0:
            raise ValueError("long break time must be an int greater than 0.")
        if type(self.work_sessions_before_long_break) is not int or self.work_sessions_before_long_break <= 0:
            raise ValueError("work sessions before long break must be an int greater than 0.")

    @classmethod
    def load_from_json(cls, json_file: Path | None = None) -> "TimerSettings":
        if json_file is None:
            json_file = Path(__file__).parent / "config.json"

        config_data = {}

        if json_file.is_file():
            try:
                with json_file.open() as f:
                    config_data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error loading config file: {e}")

        return cls(**config_data)