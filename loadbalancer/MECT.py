"""
TODO: Add Description
"""

from config import config
from loadbalancer import BaseLoadBalancer
import numpy as np


class MECT(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MECT')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def decide(self):
        """
        calculates a provisional map score for each machine
        based on the (task completion time + queue length),
        then selects a random machine from the machines with the lowest score.
        """
        if self.queue.empty():
            return None

        task = self.choose_task()
        provisional_maps = []
        for machine in config.machines:
            score = machine.compute_completion_time(task)
            provisional_maps.append((score, machine.id))

        min_score = min(provisional_maps, key=lambda x: x[0])[0]
        ties = [machine_id for score, machine_id in provisional_maps
                if score == min_score]
        selected_machine_idx = int(np.random.choice(ties[:, 1]))
        selected_machine = config.machines[selected_machine_idx]

        self.assign_task_to_machine(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
