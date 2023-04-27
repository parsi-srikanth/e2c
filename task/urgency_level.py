"""

TODO: Add description

"""

from enum import Enum, unique


@unique
class UrgencyLevel(Enum):
    BESTEFFORT = 0
    URGENT = 1
