"""
TODO: Add description
"""
from machine.machine import Machine
from machine.machine_status import MachineStatus
from machine.machine_type import MachineType
from task.task import Task
from task.task_status import TaskStatus
from task.task_type import TaskType

from abc import ABC, abstractmethod


class baseAbsEnergyModel(ABC):
    """
    TODO: Add description
    """

    def __init__(self, machine: Machine) -> None:
        super().__init__()
        self._machine = machine

    @property
    def machine(self) -> Machine:
        return self._machine

    @machine.setter
    def machine(self, machine: Machine) -> None:
        if not isinstance(machine, Machine):
            raise TypeError('Machine must be a pre-defined type')
        self._machine = machine

    @abstractmethod
    def calc_dyn_energy_consump(self, task: Task, duration: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def calc_idle_energy_consump(self, duration: float) -> float:
        raise NotImplementedError
