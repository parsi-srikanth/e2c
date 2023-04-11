"""
TODO: Add description

"""

from loadbalancer.base_loadbalancer import BaseLoadBalancer
import config.config as config


class MM(BaseLoadBalancer):

    def __init__(self, total_no_of_tasks: int):
        super().__init__()
        self.name(self, 'MM')
        self.total_no_of_tasks(self, total_no_of_tasks)

    def phase1(self):
        provisional_map = []
        index = 0
        self.prune()
        for task in self.queue.list:
            min_ct = float('inf')
            min_ct_machine = None
            for machine in config.machines:
                pct = machine.provisional_map(task)
                if pct < min_ct:
                    min_ct = pct
                    min_ct_machine = machine
            provisional_map.append([task, min_ct, min_ct_machine, index])
            index += 1
        return provisional_map

    def phase2(self, provisional_map):
        provisional_map_machines = []
        for machine in config.machines:
            if not machine.queue.full():
                min_ct = float('inf')
                task = None
                index = None
                for pair in provisional_map:
                    if pair[2] is not None \
                        and pair[2].id == machine.id \
                            and pair[1] < min_ct:
                        task = pair[0]
                        min_ct = pair[1]
                        index = pair[3]
                provisional_map_machines.append([task, machine, index])

        return provisional_map_machines

    def decide(self):
        provisional_map = self.phase1()
        provisional_map_machines = self.phase2(provisional_map)

        for pair in provisional_map_machines:
            task = pair[0]
            assigned_machine = pair[1]

            if task is not None and assigned_machine is not None:
                index = self.queue.list.index(task)
                task = self.choose_task(index)
                self.assign_task_to_machine(task, assigned_machine)
                return assigned_machine
        return None
