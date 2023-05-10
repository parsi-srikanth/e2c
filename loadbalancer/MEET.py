"""
TODO: Add description

"""

from loadbalancer import BaseLoadBalancer
import numpy as np


class MEET(BaseLoadBalancer):

    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'MEET'

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
        expected_task_machine_map = []
        for machine in self.machines:
            score = task.get_exec_time(machine.type.name)
            # TODO: add get_exec_time to task.py
            expected_task_machine_map.append((score, machine.id))

        min_score = min(expected_task_machine_map, key=lambda x: x[0])[0]
        expected_task_machine_map = np.array(expected_task_machine_map)
        ties = expected_task_machine_map[expected_task_machine_map[:, 0] == min_score]
        np.random.seed(task.id)
        selected_machine_idx = int(np.random.choice(ties[:, 1]))
        selected_machine = self.machines[selected_machine_idx]
        # check implementation of map
        self.map(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
