"""

TODO: Add description

"""

from enum import Enum, unique


@unique
class UrgencyLevel(Enum):
    BESTEFFORT = 1
    URGENT = 2