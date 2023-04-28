from config import config
from loadbalancer import BaseLoadBalancer


class LeastConnection(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MECT')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def get_next_machine(self):
        next_machine = None
        min_queue_size = float('inf')
        for machine in config.machines:
            queue_size = len(machine.queue)
            if not machine.queue.full():
                if queue_size < min_queue_size:
                    min_queue_size = queue_size
                    next_machine = machine
        if next_machine is None:
            # all machine queues are full, raise an exception
            raise Exception('All machine queues are full')
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
