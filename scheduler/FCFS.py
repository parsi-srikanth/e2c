"""
TODO: Add description
"""
from scheduler.base_abs_scheduler import baseAbsScheduler
from task.task import Task
from machine.machine import Machine
from clock import Clock


class FCFS(baseAbsScheduler):
    """
    TODO: add description
    """

    clk: Clock = Clock()

    def __init__(self, machine: Machine, qsize=0) -> None:
        super().__init__(machine, qsize)
        self.name = "FCFS"

    def admit(self, task: Task) -> None:
        if not self.is_full():
            self.queue.put(task)
        else:
            raise Exception("Queue is full")

    def pop(self):
        if not self.is_empty():
            return self.queue.get()
        else:
            return None

    def allocate(self, task: Task) -> None:
        if self.machine.is_available():
            if not isinstance(task, Task):
                raise TypeError("Task must be of type Task")
            self.machine.execute(task, self.time_slice)
        else:
            raise Exception("Machine is not available")

    def schedule(self):
        if not self.is_empty():
            task = self.pop()
            self.allocate(task)

    def q_expec_completion_time(self):
        if self.machine.is_working():
            nxt_available_time = self.machine.nxt_available_time
            for task in self.queue.queue:
                expected_completion_time = (nxt_available_time +
                                            task.expected_execution_times[
                                                self.machine.type.id])
                if expected_completion_time < task.deadline:
                    nxt_available_time = expected_completion_time
                else:
                    nxt_available_time = task.deadline
        else:
            nxt_available_time = self.clk.time
        return nxt_available_time
