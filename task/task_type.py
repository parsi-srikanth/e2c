"""

TODO: add description

"""
from abc import ABC
from urgency_level import UrgencyLevel


class TaskType(ABC):
    """
    
    TODO: add description

    """
    count = 0

    def __init__(self, urgency, hard_deadline) -> None:
        TaskType.count += 1
        self.id: int = TaskType.count
        self._name: str = f'T-{self.id}'
        self._urgency: UrgencyLevel = urgency
        self._hard_deadline: float = hard_deadline
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        if name in ['', ' ']:
            raise ValueError('Task type name cannot be either empty or'
                             'space  string ')
        self._name = name

    @property
    def urgency(self) -> UrgencyLevel:
        return self._urgency

    @urgency.setter
    def urgency(self, urgency):
        if not isinstance(urgency, UrgencyLevel):
            raise ValueError('Urgency level of the task type must'
                             'be of type UrgencyLevel')
        self._urgency = urgency
    
    @property
    def hard_deadline(self) -> float:
        return self._hard_deadline

    @hard_deadline.setter
    def hard_deadline(self, hard_deadline):
        if not isinstance(hard_deadline, float):
            raise ValueError('Hard deadline of the task type must'
                             'be a float')
        elif hard_deadline < 0:
            raise ValueError('Hard deadline of the task type cannot'
                             'be a negative value')
        self._hard_deadline = hard_deadline