"""
TODO: Add Description
"""

from enum import Enum, unique
from .event_type import EventTypes
from ..task.task import Task

class Event:
    """  An event explains different stages of processing a task, from
         arriving to completing the task.
        
         event_type: The stage of processing a task like "arriving" or 
         "completing" 
         time: It is the time of occurring an event. For example,
         time of arriving a task in "arriving" event.
         metadata: a dictionary that describes the event in detail.
    """

    def __init__(self, time, event_type, task):
        self._time: float = time
        self._event_type: EventTypes = event_type
        self._metadata: Task = task

    @property
    def time(self) -> float:
        return self._time
    
    @time.setter
    def time(self, time):
        if not isinstance(time, float):
            raise TypeError('Time of the event occuring must be a' 
                            'float value')
        elif time < 0:
            raise ValueError('Time of the event occuring cannot be'
                             'a negative value')
        self._time = time

    @property
    def event_type(self) -> EventTypes:
        return self._event_type
    
    @event_type.setter
    def event_type(self, event_type):
        if not isinstance(event_type, EventTypes):
            raise TypeError('The stage of processing a task must be a' 
                            'ENUM')
        self._event_type = event_type

    @property
    def metadata(self) -> Task:
        return self._metadata
    
    @metadata.setter
    def metadata(self, task):
        if isinstance(task, Task):
            self._metadata = task

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __gt__(self, other):
        return self.time > other.time

    def __ge__(self, other):
        return self.time >= other.time
