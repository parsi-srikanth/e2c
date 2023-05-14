"""
TODO: Add description

"""

from loadbalancer import BaseAbsLoadBalancer
from utils.descriptors import MachineList


class MM(BaseAbsLoadBalancer):

    def __init__(self, machines: MachineList, qsize=0):
        super().__init__(machines, qsize)
        self.name = 'MM'

    def generate_expected_task_machine_map(self):
        expected_task_machine_map = []
        self.prune()
        # for task in self.queue:
        #     min_ct = float('inf')
        #     min_ct_machine = None
        #     for machine in self.machines:
        #         pct = machine.scheduler.q_expec_completion_time() + \
        #             task.expected_execution_times(machine.type.id)
        #         if pct < min_ct and not machine.scheduler.is_full():
        #             min_ct = pct
        #             min_ct_machine = machine
        #     expected_task_machine_map.append((task, min_ct, min_ct_machine))
        for task in self.queue:
            min_ct_machine = min(
                (machine for machine in self.machines
                    if not machine.scheduler.is_full()),
                key=lambda machine: machine.scheduler.q_expec_completion_time()
                + task.expected_execution_times(machine.type.id),
                default=None,
            )
            if min_ct_machine is not None:
                min_ct = min_ct_machine.scheduler.q_expec_completion_time() + \
                         task.expected_execution_times(min_ct_machine.type.id)
                expected_task_machine_map.append(
                    (task, min_ct, min_ct_machine))

        return expected_task_machine_map

    def decide(self):
        expected_task_machine_map = self.generate_expected_task_machine_map()
        mapped_machines = []
        for task, _, assigned_machine in \
                sorted(expected_task_machine_map, key=lambda x: x[1]):
            if len(mapped_machines) == len(self.machines):
                break
            if assigned_machine not in mapped_machines:
                self.map(task, assigned_machine)
                mapped_machines.append(assigned_machine)
        #  use the below recursion or keep calling from the simulator
        if not self.queue.is_empty():
            self.decide()
