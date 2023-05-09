"""

TODO: add description

"""
from task.task_urgency import TaskUrgency


class TaskType:
    """
    TODO: add description
    """
    id: int = 0

    def __init__(self) -> None:
        TaskType.id += 1
        self.id = TaskType.id
        self._name: str = f'T-{self.id}'
        self._urgency: TaskUrgency = 0.0
        self._deadline: float = float('inf')

    @classmethod
    def get_id(cls) -> int:
        return cls.id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if name in ['', ' ']:
            raise ValueError('Task type name cannot be either empty or'
                             'space  string ')
        self._name = name

    @property
    def deadline(self) -> float:
        return self._deadline

    @deadline.setter
    def deadline(self, deadline) -> None:
        if not isinstance(deadline, float):
            raise TypeError('Deadline of the task type must be a'
                            'float value')
        elif deadline < 0:
            raise ValueError('Deadline of the task type cannot be'
                             'a negative value')
        self._idle_power = deadline
