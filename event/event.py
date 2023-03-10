"""
TODO: Add Description
"""

from enum import Enum, unique
from event.event_type import EventTypes
from assigned_task.assigned_task import Task

class Event:

    def __init__(self, time, event_type:EventTypes, assigned_task:Task):
        if not isinstance(time, float):
            raise TypeError('Time of the event occuring must be a' 
                            'float value')
        elif time < 0:
            raise ValueError('Time of the event occuring cannot be'
                             'a negative value')
        self._time = time
        self._event_type: EventTypes = event_type
        self._assigned_task: Task = assigned_task

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
            raise TypeError('The stage of processing a assigned task must be of' 
                            'EventType object')
        self._event_type = event_type

    @property
    def assigned_task(self) -> Task:
        return self._assigned_task
    
    @assigned_task.setter
    def assigned_task(self, assigned_task):
        if not isinstance(assigned_task, Task):
            raise TypeError('The assigned task must be of' 
                            'Task object')
            self._assigned_task = assigned_task

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
