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
        self.energy_model: EnergyModel = None
        self.completion_time = 0
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

        self.completion_time = Clock.time().value +\
            task.get_exec_time(self.machine_type)

        if Clock.time().value > task.hard_deadline:
            EventQueue.add(Event(Clock.time(), EventTypes.DROPPED, task))
            self.completion_time = Clock.time().value
            self.running = task
            return 0

        elif self.completion_time > task.hard_deadline:
            EventQueue.add(Event(task.hard_deadline, EventTypes.DROPPED, task))
            self.completion_time = task.hard_deadline
            self.running = task
            return 0

        else:
            if self.completion_time > time_share + Clock.time().value:
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
                return self.completion_time

    def preempt(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_preempted = self.running
        task_to_be_preempted.status = TaskStatus.PREEMPTED
        self.running = None
        return task_to_be_preempted

    def drop(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_dropped = self.running
        task_to_be_dropped.status = TaskStatus.DROPPED
        self.running = None
        return task_to_be_dropped

    def terminate(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_terminated = self.running
        task_to_be_terminated.status = TaskStatus.CANCELLED
        self.running = None
        return task_to_be_terminated
