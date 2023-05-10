"""
TODO: Add description

"""

from config import config_machine
from loadbalancer import BaseLoadBalancer


class MM(BaseLoadBalancer):

    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'MM'

    def generate_provisional_map(self):
        provisional_map = []
        self.prune()
        for task in self.queue.list:
            min_ct = float('inf')
            min_ct_machine = None
            for machine in config_machine.machines:
                #  pct = machine.compute_completion_time(task)
                pct = machine.scheduler.q_expec_completion_time() + \
                    task.expected_execution_times(machine.type.id)
                if pct < min_ct and not machine.scheduler.is_full():
                    min_ct = pct
                    min_ct_machine = machine
            provisional_map.append((task, min_ct, min_ct_machine))
        return provisional_map

    def decide(self):
        provisional_map = self.generate_provisional_map()
        mapped_machines = []
        for task, _, assigned_machine in \
                sorted(provisional_map, key=lambda x: x[1]):
            #  add a condition if len of mapped_machines == conf.machines
            #  then break
            if assigned_machine not in mapped_machines:
                self.assign_task_to_machine(task, assigned_machine)
                mapped_machines.append(assigned_machine)
        #  use the below recursion or keep calling from the simulator
        if not self.queue.is_empty():
            self.decide()
