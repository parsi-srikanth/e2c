"""

TODO: Add description

"""

from enum import Enum, unique


@unique
class MachineStatus(Enum):
    OFF = 0
    WORKING = 1
    IDLE = 2
