"""

TODO: Add description

"""

from enum import Enum, unique


@unique
class EventTypes(Enum):
    ARRIVING = 1
    COMPLETION = 2
    DROPPED = 3
    DEFERRED = 4
    OFFLOADED = 5