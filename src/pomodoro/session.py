from pomodoro.type_definitions import SessionType

def get_next_session(
    current_session: SessionType,
    completed_work_sessions: int
) -> SessionType:
    """Returns the next Pomodoro session type."""

    if current_session == SessionType.WORK:
        # Every 4th completed work session leads to a long break
        if completed_work_sessions > 0 and completed_work_sessions % 4 == 0:
            return SessionType.LONG_BREAK

        return SessionType.SHORT_BREAK

    if current_session in [SessionType.SHORT_BREAK, SessionType.LONG_BREAK]:
        return SessionType.WORK

    return SessionType.WORK

