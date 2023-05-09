"""
TODO: Add description.

"""
from event.event_type import EventType
from task.task import Task


class Event:
    """
    TODO: Add description.
    """

    def __init__(self, type: EventType, time: float, task: Task):
        if not isinstance(type, EventType):
            raise TypeError("Event type must be of type EventType")
        elif not (isinstance(time, float) or isinstance(time, int)):
            raise TypeError("Time must be of type float")
        elif time < 0:
            raise ValueError("Time must be non-negative")
        elif not isinstance(task, Task):
            raise TypeError("Task must be of type Task")
        self._time: float = time
        self._type: EventType = type
        self._task: Task = task

    @property
    def time(self) -> float:
        return self._time

    @time.setter
    def time(self, time: float):
        if not (isinstance(time, float) or isinstance(time, int)):
            raise TypeError("Time must be of type float")
        elif time < 0:
            raise ValueError("Time must be non-negative")
        self._time = time

    @property
    def type(self) -> EventType:
        return self._type

    @type.setter
    def type(self, type: EventType):
        if not isinstance(type, EventType):
            raise TypeError("Event type must be of type EventType")
        self._type = type

    @property
    def task(self) -> Task:
        return self._task

    @task.setter
    def task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("Task must be of type Task")
        self._task = task

    def __eq__(self, other):
        return self._time == other._time

    def __ne__(self, other):
        return self._time != other._time

    def __lt__(self, other):
        return self._time < other._time

    def __le__(self, other):
        return self._time <= other._time

    def __gt__(self, other):
        return self._time > other._time

    def __ge__(self, other):
        return self._time >= other._time
