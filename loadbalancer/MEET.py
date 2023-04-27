"""
TODO: Add description

"""

from config import config
from loadbalancer import BaseLoadBalancer
import numpy as np


class MEET(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MEET')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def decide(self):
        """
        calculates a provisional map score for each machine
        based on the task (estimated time),
        then selects a random machine from the machines with the lowest score.
        """
        if self.queue.empty():
            return None

        task = self.choose_task()
        ties = []
        provisional_maps = []
        for machine in config.machines:
            score = task.get_exec_time(machine.type.name)
            # TODO: add get_exec_time to task.py
            provisional_maps.append((score, machine.id))

        min_score = min(provisional_maps, key=lambda x: x[0])[0]
        provisional_maps = np.array(provisional_maps)
        ties = provisional_maps[provisional_maps[:, 0] == min_score]
        np.random.seed(task.id)
        selected_machine_idx = int(np.random.choice(ties[:, 1]))
        selected_machine = config.machines[selected_machine_idx]
        # check implementation of assign_task_to_machine
        self.assign_task_to_machine(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
