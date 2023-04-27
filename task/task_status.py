"""
TODO: Add description
"""

from enum import Enum, unique


@unique
class TaskStatus(Enum):
    ARRIVING = 1
    CANCELLED = 2
    PENDING = 3
    RUNNING = 4
    PREEMPTED = 5
    COMPLETED = 6
    XCOMPLETED = 7
    OFFLOADED = 8
    DEFERRED = 9
    DROPPED = 10
