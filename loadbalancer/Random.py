from config import config
from loadbalancer import BaseLoadBalancer
import random


class Random(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int, N: int):
        super().__init__()
        self.name(self, 'MECT')
        self.total_no_of_tasks(self, total_no_of_tasks)
        self.N = N

    def get_next_machine(self):
        selected_machines = random.sample(config.machines, self.N)
        next_machine = min(selected_machines, key=lambda m: len(m.queue))
        if next_machine.queue.full():
            # selected machine's queue is full, try again
            return self.get_next_machine()
        else:
            return next_machine

    def decide(self):
        if self.queue.empty():
            return None

        task = self.choose_task()
        selected_machine = self.get_next_machine()
        self.assign_task_to_machine(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
