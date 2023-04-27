"""

TODO: add description

"""
from clock import Clock
from event import Event, EventTypes, EventQueue
from machine.machine_status import MachineStatus
from power import EnergyModel
from task import Task, TaskStatus


class Machine:
    def __init__(self):
        super().__init__()
        self.energyModel: EnergyModel = None
        self.completionTime = 0
        self.start()

    def execute(self, task: Task, time_share: float) -> float:
        if not isinstance(task, Task):
            raise TypeError('Task is unknown')
        if not isinstance(time_share, float):
            raise TypeError('Time share must be a float value')
        elif time_share < 0:
            raise ValueError('Time share cannot be a negative value')

        if self.status != MachineStatus.IDLE:
            raise RuntimeError('Machine is not idle')
        if self.running is not None:
            raise RuntimeError('Machine is already running a task')

        self.completionTime = Clock.time().value +\
            task.get_exec_time(self.machine_type)

        if Clock.time().value > task.hard_deadline:
            EventQueue.add(Event(Clock.time(), EventTypes.DROPPED, task))
            self.completionTime = Clock.time().value
            self.running = task
            return 0

        elif self.completionTime > task.hard_deadline:
            EventQueue.add(Event(task.hard_deadline, EventTypes.DROPPED, task))
            self.completionTime = task.hard_deadline
            self.running = task
            return 0

        else:
            if self.completionTime > time_share + Clock.time().value:
                EventQueue.add(Event(
                        time_share + Clock.time().value,
                        EventTypes.DEFERRED,
                        task))
                self.running = task
                self.status = MachineStatus.WORKING
                return time_share + Clock.time().value
            else:
                EventQueue.add(Event(
                    Clock.time(),
                    EventTypes.COMPLETION,
                    task))
                self.running = task
                self.status = MachineStatus.WORKING
                return self.completionTime

    def preempt(self) -> Task:
        self.status = MachineStatus.IDLE
        taskToBePreempted = self.running
        taskToBePreempted.status = TaskStatus.Preempted
        self.running = None
        return taskToBePreempted

    def drop(self) -> Task:
        self.status = MachineStatus.IDLE
        taskToBeDropped = self.running
        taskToBeDropped.status = 'dropped'
        self.running = None
        return taskToBeDropped

    def terminate(self) -> Task:
        self.status = MachineStatus.IDLE
        taskToBeTerminated = self.running
        taskToBeTerminated.status = 'cancelled'
        self.running = None
        return taskToBeTerminated
