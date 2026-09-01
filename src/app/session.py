import helpers

def build_session_schedule(sessions):
    """Builds a schedule from an array of strings"""
    lines = ["Schedule:"]

    for order_num, session in enumerate(sessions, start=1):
        # add to schedule
        lines.append(f"{order_num}. {session}")

    return lines

def print_schedule(schedule):
    for line in schedule:
        print(line)
    print()

def get_session_duration(session_name, session_data):
    """Gets the formatted duration of a session"""
    session_info = session_data.get(session_name)
    duration_secs = helpers.minutes_to_seconds(session_info.get("duration", 0))

    return helpers.format_time(duration_secs)


