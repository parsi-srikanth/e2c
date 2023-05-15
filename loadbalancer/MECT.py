"""
TODO: Add Description
"""

from loadbalancer import BaseAbsLoadBalancer
import numpy as np


class MECT(BaseAbsLoadBalancer):

    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'MECT'

    def decide(self):
        """
        calculates a provisional map score for each machine
        based on the (task completion time + queue length),
        then selects a random machine from the machines with the lowest score.
        """
        if self.queue.empty():
            return None

        task = self.choose_task()
        expected_task_machine_map = []
        for machine in self.machines:
            score = machine.compute_completion_time(task)
            expected_task_machine_map.append((score, machine.id))

        min_score = min(expected_task_machine_map, key=lambda x: x[0])[0]
        ties = [machine_id for score, machine_id in expected_task_machine_map
                if score == min_score]
        selected_machine_idx = int(np.random.choice(ties[:, 1]))
        selected_machine = self.machines[selected_machine_idx]

        self.map(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
