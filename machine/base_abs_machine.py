"""
TODO: Add description
"""
from abc import ABC, abstractmethod

from task.task import Task
from utils.descriptors import FloatDict, IntDict, IntDictIntList, IntList
from clock import Clock
from machine.machine_type import MachineType
from machine.machine_status import MachineStatus
from scheduler.base_abs_scheduler import baseAbsScheduler


class baseAbsMachine(ABC):
    """
    TODO: Class description
    """
    clk: Clock = Clock()
    id: int = 0

    def __init__(self, machine_type: MachineType) -> None:
        super().__init__()
        baseAbsMachine.id += 1
        self._id = baseAbsMachine.id
        self._machine_type: MachineType = machine_type
        self._scheduler = None
        self._status: MachineStatus = MachineStatus.OFF
        self._nxt_available_time: float = 0.0
        self._running_task: Task = None
        self._energy_usuage: FloatDict = FloatDict({
            "dynamic": 0.0,
            "idle": 0.0,
            "wasted": 0.0,
            "total": 0.0
        })

        self._processed_tasks: IntDictIntList = IntDict({
            'completed': IntList(),
            'dropped': IntList(),
            'executed': IntList(),
            }
        )

    def __repr__(self) -> str:
        return f'Machine {self.id}'

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id) -> None:
        if not isinstance(id, int):
            raise TypeError('Machine ID must be an integer')
        self._id = id

    @property
    def machine_type(self) -> MachineType:
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type: MachineType) -> None:
        if not isinstance(machine_type, MachineType):
            raise TypeError('Machine type must be a pre-defined type')
        self._machine_type = machine_type

    @property
    def scheduler(self):
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """
        TODO: Change baseABsScheduler to Scheduler
        """
        if not isinstance(scheduler, baseAbsScheduler):
            raise TypeError("Scheduler must be of type baseAbsScheduler")
        self._scheduler = scheduler

    @property
    def status(self) -> MachineStatus:
        return self._status

    @status.setter
    def status(self, machine_status: MachineStatus) -> None:
        if not isinstance(machine_status, MachineStatus):
            raise TypeError('Machine status is unknown')
        self._status = machine_status

    @property
    def nxt_available_time(self) -> float:
        return self._nxt_available_time

    @nxt_available_time.setter
    def nxt_available_time(self, nxt_available_time: float) -> None:
        if not nxt_available_time >= 0:
            raise ValueError('Next available time cannot be negative')
        self._nxt_available_time = nxt_available_time

    @property
    def running_task(self) -> Task:
        return self._running_task

    @running_task.setter
    def running_task(self, task: Task) -> None:
        if not (isinstance(task, Task) or None):
            raise TypeError('Running task must be a task or None')
        self._running_task = task

    @property
    def energy_usuage(self) -> FloatDict:
        return self._energy_usuage

    @energy_usuage.setter
    def energy_usuage(self, energy_usuage: FloatDict) -> None:
        if not isinstance(energy_usuage, FloatDict):
            raise TypeError('Energy usuage must be a FloatDict')
        self._energy_usuage = energy_usuage

    @property
    def processed_tasks(self) -> IntDictIntList:
        return self._processed_tasks

    @processed_tasks.setter
    def processed_tasks(self, processed_tasks: IntDictIntList) -> None:
        if not isinstance(processed_tasks, IntDictIntList):
            raise TypeError('Processed tasks must be a IntDictIntList')
        self._processed_tasks = processed_tasks

    def start(self) -> None:
        self.status = MachineStatus.WORKING

    def shutdown(self) -> None:
        self.status = MachineStatus.OFF

    def idle(self) -> None:
        self.status = MachineStatus.IDLE

    def is_working(self) -> bool:
        return self.status == MachineStatus.WORKING

    def is_available(self) -> bool:
        return self.status == MachineStatus.IDLE

    def is_off(self) -> bool:
        return self.status == MachineStatus.OFF

    @abstractmethod
    def execute(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def preempt(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def terminate(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def drop(self, task: Task) -> None:
        raise NotImplementedError
