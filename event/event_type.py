"""

TODO: Add description

"""

from enum import Enum, unique
from typing import Literal


@unique
class EventType(Enum):
    ARRIVING: Literal[0] = 0
    COMPLETION: Literal[1] = 1
    DROPPING: Literal[2] = 2
    DEFERRING: Literal[3] = 3
    PREEMPTION: Literal[4] = 4
    OFFLOADING: Literal[5] = 5

    def __str__(self) -> str:
        return self.name
