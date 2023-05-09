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

    def __init__(self, machine: Machine, timeslice: float = float('inf'),
                 qsize=0) -> None:
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
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

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

    @abstractmethod
    def q_expec_completion_time(self):
        raise NotImplementedError
