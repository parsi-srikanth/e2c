"""
TODO: Add Description
"""

from loadbalancer import BaseLoadBalancer


class MSD(BaseLoadBalancer):
    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name = 'MSD'
        self.total_no_of_tasks(self, total_no_of_tasks)

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
            expected_task_machine_map.append((task, min_ct, min_ct_machine))
        return expected_task_machine_map

    def decide(self):
        expected_task_machine_map = self.generate_expected_task_machine_map()
        for machine in self.machines:
            if not machine.queue.full():
                soonest_deadline = float('inf')
                task = None
                for pair in expected_task_machine_map:
                    if pair[2] is not None \
                        and pair[2].id == machine.id \
                            and pair[0].deadline < soonest_deadline:
                        task = pair[0]
                        soonest_deadline = task.hard_deadline
                if task is not None:
                    self.map(task, machine)
                    return machine

        return None
