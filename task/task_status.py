"""

TODO: Add description

"""

from enum import Enum, unique
from typing import Literal


@unique
class TaskStatus(Enum):
    ARRIVING: Literal[0] = 0
    CANCELLED: Literal[1] = 1
    PENDING: Literal[2] = 2
    RUNNING: Literal[3] = 3
    COMPLETED: Literal[4] = 4
    PREEMPTED: Literal[5] = 5
    XCOMPLETED: Literal[6] = 6
    OFFLOADED: Literal[7] = 7
    DEFERRED: Literal[8] = 8
    DROPPED: Literal[9] = 9

    def __str__(self) -> str:
        return self.name
