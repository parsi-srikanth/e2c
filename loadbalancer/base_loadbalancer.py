"""
TODO: Add description
"""
from abs import ABC
from clock import Clock
from event import Event, EventTypes, EventQueue
from Task import TaskStatus, Task
from utils.descriptors import IntDict, IntDictIntList, IntList, QTask


class baseAbsLoadBalancer(ABC):
    """
    TODO: AddClass description
    """

    task_to_be_actioned = None
    clk: Clock = Clock()

    def __init__(self, qsize=0) -> None:
        super().__init__()
        self.queue = QTask(maxsize=qsize)
        self._name = 'base'
        self.stats: IntDictIntList = IntDict({
            'drop': IntList(),
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

    def get_stats(self):
        return self.stats

    def is_empty(self):
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

    def choose_task(self, index=0):
        task_to_be_actioned = self.queue.list[index]
        return task_to_be_actioned

    def defer(self, task):
        if self.clk.time > task.hard_deadline:
            self.drop(task)
            return 1
        self.task_to_be_actioned = None
        task.status = TaskStatus.DEFERRED
        task.no_of_deferring += 1
        self.stats['deferred'].append(task)
        event_time = EventQueue.event_list[0].time
        event_type = EventTypes.DEFERRED
        event = Event(event_time, event_type, task)
        EventQueue.add_event(event)

    def drop(self, task):
        self.task_to_be_actioned = None
        task.status = TaskStatus.CANCELLED
        task.drop_time = self.clk.time
        self.stats['dropped'].append(task)
        self.queue.pop(task)

    def assign_task_to_machine(self, task, machine):
        if not isinstance(task, Task):
            raise TypeError("Task must be of type Task")
        assignment = machine.scheduler.admit(task)
        if assignment is not False:
            task.assigned_machine = machine
            task.status = TaskStatus.MAPPED
            self.stats['mapped'].append(task)
            self.queue.pop(task)
        else:
            self.defer(task)

    def prune(self):
        for task in self.queue.list:
            if self.clk.time > task.hard_deadline:
                task.status = TaskStatus.CANCELLED
                task.drop_time = self.clk.time
                self.stats['dropped'].append(task)
                self.queue.pop(task)

    def decide():
        raise NotImplementedError("Please Implement this method")
