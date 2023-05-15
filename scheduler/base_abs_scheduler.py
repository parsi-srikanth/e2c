"""
TODO: Add description
"""
from utils.descriptors import QTask
from task.task import Task
from machine.machine import Machine
from abc import ABC, abstractmethod


class baseAbsScheduler(ABC):
    """
    TODO: Class description
    """

    def __init__(self, machine: Machine, qsize=0,
                 timeslice: float = float('inf')) -> None:
        super().__init__()
        self.name = None
        self.queue = QTask(maxsize=qsize)
        if not isinstance(machine, Machine):
            raise TypeError("Machine must be of type Machine")
        self._machine = machine
        if not isinstance(timeslice, float):
            raise TypeError("Timeslice must be of type float")
        elif timeslice <= 0:
            raise ValueError("Timeslice must be positive")
        self._time_slice = timeslice

    @property
    def machine(self):
        return self._machine

    @machine.setter
    def machine(self, machine):
        if not isinstance(machine, Machine):
            raise TypeError("Machine must be of type Machine")
        self._machine = machine

    @property
    def time_slice(self):
        return self._time_slice

    @time_slice.setter
    def time_slice(self, timeslice):
        if not isinstance(timeslice, float):
            raise TypeError("Timeslice must be of type float")
        elif timeslice <= 0:
            raise ValueError("Timeslice must be positive")
        self._time_slice = timeslice

    def is_empty(self):
        return len(self.queue.list) == 0

    def is_full(self):
        return len(self.queue.list) == self.queue.maxsize

    @abstractmethod
    def schedule(self):
        raise NotImplementedError

    @abstractmethod
    def admit(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> Task:
        raise NotImplementedError

    @abstractmethod
    def allocate(self, task: Task) -> None:
        raise NotImplementedError

#  Modified by : Srikanth
    @abstractmethod
    def q_expec_completion_time(self, machine):
        raise NotImplementedError
