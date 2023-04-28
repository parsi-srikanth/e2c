"""
TODO: Add description
"""
from abs import ABC
from machine.machine_type import MachineType
from machine.machine_status import MachineStatus
from task import Task


class baseAbsMachine(ABC):
    """
    TODO: Class description
    """
    count = 0

    def __init__(self, machine_type: MachineType) -> None:
        super().__init__()
        baseAbsMachine.count += 1
        self._id = baseAbsMachine.count
        self._machine_type: MachineType = machine_type
        self._status: MachineStatus = MachineStatus.OFF
        self._running_task: Task = None
        self._throughput: float = 0
        self._available_time: float = 0
        self._energy_consumption = {
            'idle': 0,
            'working': 0,
            'wasted': 0
            }

    @property
    def machine_type(self) -> MachineType:
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type: MachineType):
        if not isinstance(machine_type, MachineType):
            raise TypeError('Machine type must be a pre-defined type')
        self._machine_type = machine_type

    @property
    def status(self) -> MachineStatus:
        return self._status

    @status.setter
    def status(self, machine_status: MachineStatus):
        if not isinstance(machine_status, MachineStatus):
            raise TypeError('Machine status is unknown')
        self._status = machine_status

    @property
    def running_task(self) -> Task:
        return self._running_task

    @running_task.setter
    def running_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError('Task is unknown')
        self._running_task = task

    @property
    def throughput(self) -> float:
        return self._throughput

    @throughput.setter
    def throughput(self, throughput: float):
        if not isinstance(throughput, float):
            raise TypeError('Throughput must be a float value')
        elif throughput < 0:
            raise ValueError('Throughput cannot be a negative value')
        self._throughput = throughput

    @property
    def available_time(self) -> float:
        return self._available_time

    @available_time.setter
    def available_time(self, available_time: float):
        if not isinstance(available_time, float):
            raise TypeError('Available time must be a float value')
        elif available_time < 0:
            raise ValueError('Available time cannot be a negative value')
        self._available_time = available_time

    @property
    def energy_consumption(self) -> dict:
        return self._energy_consumption

    @energy_consumption.setter
    def energy_consumption(self, energy_consumption: dict):
        if not isinstance(energy_consumption, dict):
            raise TypeError('Energy consumption must be a dictionary')
        self._energy_consumption = energy_consumption

    def start(self):
        self.status = MachineStatus.IDLE

    def reset(self):
        self.status = MachineStatus.IDLE
        self.running_task = None
        self.throughput = 0
        self.available_time = 0
        self.energy_consumption = {
            'idle': 0,
            'working': 0,
            'wasted': 0
            }

    def is_working(self) -> bool:
        return self.status == MachineStatus.WORKING

    def info(self) -> dict:
        return {
            'machine_type': self.machine_type,
            'status': self.status,
            'running_task': self.running_task,
            'throughput': self.throughput,
            'available_time': self.available_time,
            'energy_consumption': self.energy_consumption
            }

    def shutdown(self):
        self.status = MachineStatus.OFF
