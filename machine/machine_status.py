"""

TODO: Add description

"""

from enum import Enum, unique
from typing import Literal


@unique
class MachineStatus(Enum):
    OFF: Literal[0] = 0
    WORKING: Literal[1] = 1
    IDLE: Literal[2] = 2

    def __str__(self) -> str:
        return self.name
