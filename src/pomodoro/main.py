from timer import PomodoroTimer


if __name__ == "__main__":
    # Define the schedule sequence
    configured_schedule: tuple[str, ...] = (
        "Work session", "Short break",
        "Work session", "Short break",
        "Work session", "Short break",
        "Work session", "Long break"
    )
    configured_session_times:list[int] = [1, 1, 1]

    timer = PomodoroTimer(schedule=configured_schedule,
                          work_time=configured_session_times[0],
                          short_break_time=configured_session_times[1],
                          long_break_time=configured_session_times[2])


