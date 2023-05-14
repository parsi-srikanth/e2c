"""
TODO: Add Description
"""

from loadbalancer import BaseAbsLoadBalancer


class MMU(BaseAbsLoadBalancer):
    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'MMU'

    def generate_expected_task_machine_map(self):
        expected_task_machine_map = []
        self.prune()
        for task in self.queue.list:
            min_ct = float('inf')
            min_ct_machine = None
            for machine in self.machines:
                pct = machine.compute_completion_time(task)
                if pct < min_ct and not machine.queue.full():
                    min_ct = pct
                    min_ct_machine = machine
            slack = task.hard_deadline - min_ct
            if slack == 0:
                urgency = float('inf')
            else:
                urgency = 1 / slack
            expected_task_machine_map.append(
                (task, min_ct, min_ct_machine, urgency))
        return expected_task_machine_map

    def decide(self):
        expected_task_machine_map = self.generate_expected_task_machine_map()
        # Sorting the provisional map by urgency (in descending order)
        # and then by minimum completion time (in ascending order).
        for task, _, assigned_machine, _, _ in \
                sorted(expected_task_machine_map, key=lambda x: (-x[3], x[1])):
            if assigned_machine is not None:
                self.map(task, assigned_machine)
                return assigned_machine
        return None
