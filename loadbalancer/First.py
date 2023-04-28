from config import config
from loadbalancer import BaseLoadBalancer


class FIRST(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MECT')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def get_next_machine(self):
        lowest_id = float('inf')
        next_machine = None
        for machine in config.machines:
            if machine.id < lowest_id and not machine.queue.full():
                lowest_id = machine.id
                next_machine = machine
        if next_machine is None:
            # all machine queues are full, increment id and try again
            config.machine_id = (config.machine_id + 1)/len(config.machines)
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
