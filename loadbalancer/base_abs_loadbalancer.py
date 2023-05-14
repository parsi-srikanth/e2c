"""
TODO: Add description
"""
from abc import ABC, abstractmethod
from clock import Clock
from task import TaskStatus, Task
from utils.descriptors import IntDictIntList, IntList, MachineList, QTask


class BaseAbsLoadBalancer(ABC):
    """
    TODO: AddClass description
    """

    clk: Clock = Clock()

    def __init__(self, machines, qsize=0) -> None:
        super().__init__()
        if not isinstance(machines, MachineList):
            raise TypeError('message')
        self._machines: MachineList = machines
        self.queue = QTask(maxsize=qsize)
        self._name = 'base'
        self.stats: IntDictIntList = IntDictIntList({
            'deferred': IntList(),
            'cancelled': IntList(),
            'mapped': IntList()
            }
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def machines(self):
        return self._machines

    @machines.setter
    def machines(self, machines: MachineList):
        self._machines = machines

    def get_stats(self):
        return self.stats

    def is_empty(self):
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

    def choose_task(self, index=0):
        queue_list = list(self.queue)
        return queue_list[index]

    def defer(self, task):
        if self.clk.time > task.hard_deadline:
            self.drop(task)
            return 1
        task.status = TaskStatus.DEFERRED
        task.no_of_deferring += 1
        self.stats['deferred'].append(task)

    def drop(self, task):
        task.status = TaskStatus.CANCELLED
        task.drop_time = self.clk.time
        self.stats['dropped'].append(task)
        self.queue.remove(task)

    def map(self, task, machine):
        if not isinstance(task, Task):
            raise TypeError("Task must be of type Task")
        assignment = machine.scheduler.admit(task)
        if assignment is not False:
            task.assigned_machine = machine
            task.status = TaskStatus.MAPPED
            self.stats['mapped'].append(task)
            self.queue.remove(task)
        else:
            self.defer(task)

    def prune(self):
        for task in self.queue.list:
            if self.clk.time > task.hard_deadline:
                task.status = TaskStatus.CANCELLED
                task.drop_time = self.clk.time
                self.stats['dropped'].append(task)
                self.queue.remove(task)

    @abstractmethod
    def decide():
        raise NotImplementedError("Please Implement this method")
