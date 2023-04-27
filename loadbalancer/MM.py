"""
TODO: Add description

"""

from config import config
from loadbalancer import BaseLoadBalancer


class MM(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MM')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def generate_provisional_map(self):
        provisional_map = []
        self.prune()
        for task in self.queue.list:
            min_ct = float('inf')
            min_ct_machine = None
            for machine in config.machines:
                pct = machine.compute_completion_time(task)
                if pct < min_ct and not machine.queue.full():
                    min_ct = pct
                    min_ct_machine = machine
            provisional_map.append((task, min_ct, min_ct_machine))
        return provisional_map

    def decide(self):
        provisional_map = self.generate_provisional_map()
        for task, _, assigned_machine in \
                sorted(provisional_map, key=lambda x: x[1]):
            if assigned_machine is not None:
                self.assign_task_to_machine(task, assigned_machine)
                return assigned_machine
        return None
