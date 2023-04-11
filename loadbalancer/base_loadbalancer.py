"""
TODO: Add description
"""
from abs import ABC
import clock as clock
import config.config as config
from event import Event, EventTypes
import queue as Queue
import TaskStatus as TaskStatus


class baseAbsLoadBalancer(ABC):
    """
    TODO: AddClass description
    """

    taskToBeActioned = None

    def __init__(self) -> None:
        super().__init__()
        self.queue = Queue()
        self._name = 'base'
        self._total_no_of_tasks = 0
        self.stats = {
            'drop': [],
            'deferred': [],
            'cancelled': [],
            'mapped': []
            }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def total_no_of_tasks(self):
        return self._total_no_of_tasks

    @total_no_of_tasks.setter
    def total_no_of_tasks(self, total_no_of_tasks):
        if not isinstance(total_no_of_tasks, int):
            raise TypeError('total no of tasks must be a'
                            'integer value')
        elif total_no_of_tasks < 0:
            raise ValueError('total no of tasks cannot be'
                             'a negative value')
        self._total_no_of_tasks = total_no_of_tasks

    def get_stats(self):
        return self.stats

    def get_queue(self):
        return self.queue

    def isempty(self):
        return self.queue.isempty()

    def choose_task(self, index=0):
        taskToBeActioned = self.queue.get(index)
        return taskToBeActioned

    def defer(self, task):
        if clock.time() > task.deadline:
            self.drop(task)
            return 1
        self.taskToBeActioned = None
        task.status = TaskStatus.DEFERRED
        task.no_of_deferring += 1
        self.queue.put(task)
        self.stats['deferred'].append(task)
        event_time = config.event_queue.event_list[0].time
        event_type = EventTypes.DEFERRED
        event = Event(event_time, event_type, task)
        config.event_queue.add_event(event)

    def drop(self, task):
        self.taskToBeActioned = None
        task.status = TaskStatus.CANCELLED
        task.drop_time = clock.time()
        self.stats['dropped'].append(task)
        self.queue.remove(task)

    def assign_task_to_machine(self, task, machine):
        task = self.choose_task() if self.taskToBeActioned is None \
            else self.taskToBeActioned
        assignment = machine.admit(task)
        if assignment != 'notEmpty':
            task.assigned_machine = machine
            self.stats['mapped'].append(task)
            task.status = TaskStatus.MAPPED
        else:
            self.defer(task)

    def prune(self):
        for task in self.queue.list:
            if clock.time() > task.deadline:
                task.status = TaskStatus.CANCELLED
                task.drop_time = clock.time()
                self.stats['dropped'].append(task)
                self.queue.remove(task)

    def decide():
        raise NotImplementedError("Please Implement this method")
