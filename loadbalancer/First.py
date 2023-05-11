from loadbalancer import BaseLoadBalancer


class FIRST(BaseLoadBalancer):

    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'First'

    def get_next_machine(self):
        lowest_id = float('inf')
        next_machine = None
        for machine in self.machines:
            if machine.id < lowest_id and not machine.queue.full():
                lowest_id = machine.id
                next_machine = machine
        if next_machine is None:
            # all machine queues are full, increment id and try again
            machine.machine_id = (machine.machine_id + 1)/len(self.machines)
            return self.get_next_machine()
        else:
            return next_machine

    def decide(self):
        if self.queue.empty():
            return None

        task = self.choose_task()
        selected_machine = self.get_next_machine()
        self.map(task, selected_machine)
        self.queue.remove(task)
        return selected_machine
