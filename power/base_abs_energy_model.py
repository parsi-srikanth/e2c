"""
TODO: Add description
"""
from task.task import Task

from abc import ABC, abstractmethod


class baseAbsEnergyModel(ABC):
    """
    TODO: Add description
    """

    def __init__(self, machine) -> None:
        super().__init__()
        self._machine = machine

    @property
    def machine(self):
        return self._machine

    @machine.setter
    def machine(self, machine) -> None:
        #  Modified by : Srikanth
        # if not isinstance(machine, Machine):
        #     raise TypeError('Machine must be a pre-defined type')
        self._machine = machine

    @abstractmethod
    def calc_dyn_energy_consump(self, task: Task, duration: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def calc_idle_energy_consump(self, duration: float) -> float:
        raise NotImplementedError
