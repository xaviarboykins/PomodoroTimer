from enum import Enum

class SessionType(Enum):
    IDLE = 0
    WORK = 1
    SHORT_BREAK = 2
    LONG_BREAK = 3