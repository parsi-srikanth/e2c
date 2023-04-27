"""
TODO: Add Description
"""

from task import UrgencyLevel


class TaskType:

    count = 0

    def __init__(self, name: str, urgency: UrgencyLevel,
                 hard_deadline: float) -> None:
        self._id: int = TaskType.count+1
        self._name: str = name
        self._urgency: UrgencyLevel = urgency
        self._hard_deadline: float = hard_deadline

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def urgency(self) -> UrgencyLevel:
        return self._urgency

    @property
    def hard_deadline(self) -> float:
        return self._hard_deadline

    @name.setter
    def name(self, name: str):
        if name in ['', ' ']:
            raise ValueError('Task type name cannot be either empty or'
                             'space  string ')
        self._name = name

    @urgency.setter
    def urgency(self, urgency: UrgencyLevel):
        if not isinstance(urgency, UrgencyLevel):
            raise TypeError('Urgency level must be a pre-defined type')
        self._urgency = urgency

    @hard_deadline.setter
    def hard_deadline(self, hard_deadline: float):
        if not isinstance(hard_deadline, float):
            raise TypeError('Hard deadline must be a float value')
        elif hard_deadline < 0:
            raise ValueError('Hard deadline cannot be a negative value')
        self._hard_deadline = hard_deadline
