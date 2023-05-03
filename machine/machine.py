"""

TODO: add description

"""
from clock import Clock
from event import Event, EventTypes, EventQueue
from machine.machine_status import MachineStatus
from power import EnergyModel
from task import Task, TaskStatus
import queue as Queue


class Machine:
    def __init__(self):
        super().__init__()
        self.energy_model: EnergyModel = None
        self.completion_time = 0
        self.running_task: Task = None
        self.queue = Queue()
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
        if self.running_task is not None:
            raise RuntimeError('Machine is already running a task')

        self.completion_time = Clock.time().value +\
            task.get_exec_time(self.machine_type)

        if Clock.time().value > task.hard_deadline:
            EventQueue.add(Event(Clock.time(), EventTypes.DROPPED, task))
            self.completion_time = Clock.time().value
            self.running_task = task
            return 0

        elif self.completion_time > task.hard_deadline:
            EventQueue.add(Event(task.hard_deadline, EventTypes.DROPPED, task))
            self.completion_time = task.hard_deadline
            self.running_task = task
            return 0

        else:
            if self.completion_time > time_share + Clock.time().value:
                EventQueue.add(Event(
                        time_share + Clock.time().value,
                        EventTypes.PREEMPTION,
                        task))
                self.running_task = task
                self.status = MachineStatus.WORKING
                return time_share + Clock.time().value
            else:
                EventQueue.add(Event(
                    Clock.time(),
                    EventTypes.COMPLETION,
                    task))
                self.running_task = task
                self.status = MachineStatus.WORKING
                return self.completion_time

    def preempt(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_preempted = self.running_task
        task_to_be_preempted.status = TaskStatus.PREEMPTED
        self.running_task = None
        return task_to_be_preempted

    def drop(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_dropped = self.running_task
        task_to_be_dropped.status = TaskStatus.DROPPED
        self.running_task = None
        return task_to_be_dropped

    def terminate(self) -> Task:
        self.status = MachineStatus.IDLE
        task_to_be_terminated = self.running_task
        task_to_be_terminated.status = TaskStatus.CANCELLED
        self.running_task = None
        return task_to_be_terminated

    def compute_completion_time(self, task) -> float:
        if not isinstance(task, Task):
            raise TypeError('Task is unknown')
        for t in self.queue:
            self.completion_time += t.get_exec_time(self.machine_type)

        return task.get_exec_time(self.machine_type) + Clock.time().value +\
            self.completion_time
