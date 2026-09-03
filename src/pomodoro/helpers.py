# Calculations
def minutes_to_seconds(minutes):
    """Converts a minutes into a number of seconds"""
    return minutes * 60

# Formatting time
def format_time(seconds):
    """Formats seconds into a visually understandable format returning MM:SS"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"