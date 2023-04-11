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
        self._running: Task = None  # why do we need a task here?
        self._throughput: float = 0
        self._availableTime: float = 0
        self._queueSize: int = 0  # This is needed but not in class diagram
        self._energyConsumption = {
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
    def running(self) -> Task:
        return self._running

    @running.setter
    def running(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError('Task is unknown')
        self._running = task

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
    def availableTime(self) -> float:
        return self._availableTime

    @availableTime.setter
    def availableTime(self, availableTime: float):
        if not isinstance(availableTime, float):
            raise TypeError('Available time must be a float value')
        elif availableTime < 0:
            raise ValueError('Available time cannot be a negative value')
        self._availableTime = availableTime

    @property
    def energyConsumption(self) -> dict:
        return self._energyConsumption

    @energyConsumption.setter
    def energyConsumption(self, energyConsumption: dict):
        if not isinstance(energyConsumption, dict):
            raise TypeError('Energy consumption must be a dictionary')
        self._energyConsumption = energyConsumption

    @property
    def queueSize(self) -> int:
        return self._queueSize

    @queueSize.setter
    def queueSize(self, queueSize: int):
        if not isinstance(queueSize, int):
            raise TypeError('Queue size must be an integer')
        elif queueSize < 0:
            raise ValueError('Queue size cannot be a negative value')
        self._queueSize = queueSize

    def start(self):
        self.status = MachineStatus.WORKING

    def reset(self):
        self.status = MachineStatus.OFF
        self.running = None
        self.throughput = 0
        self.availableTime = 0
        self.energyConsumption = {
            'idle': 0,
            'working': 0,
            'wasted': 0
            }

    def is_working(self) -> bool:
        return self.status == MachineStatus.WORKING

    def execute(self, task: Task, time_share: float) -> float:
        if not isinstance(task, Task):
            raise TypeError('Task is unknown')
        if not isinstance(time_share, float):
            raise TypeError('Time share must be a float value')
        elif time_share < 0:
            raise ValueError('Time share cannot be a negative value')

        self.running = task
        self.throughput = time_share  # how is this calculated?
        self.availableTime = time_share  # what is this?
        self.status = MachineStatus.WORKING
        return time_share

    def preempt(self):  # what should be the return type?
        self.status = MachineStatus.IDLE
        self.running = None
        self.throughput = 0
        self.availableTime = 0

    def drop(self):  # what should be the return type?
        self.status = MachineStatus.IDLE
        self.running = None
        self.throughput = 0
        self.availableTime = 0

    def terminate(self):  # what should be the return type?
        self.status = MachineStatus.OFF
        self.running = None
        self.throughput = 0
        self.availableTime = 0

    def info(self) -> dict:
        return {
            'machine_type': self.machine_type,
            'status': self.status,
            'running': self.running,
            'throughput': self.throughput,
            'availableTime': self.availableTime,
            'energyConsumption': self.energyConsumption
            }

    def shutdown(self):  # why is this needed we already have terminate?
        self.status = MachineStatus.OFF
