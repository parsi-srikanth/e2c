from loadbalancer import BaseLoadBalancer


class LeastConnection(BaseLoadBalancer):

    def __init__(self, qsize=0):
        super().__init__(qsize)
        self.name = 'LeastConnection'

    def get_next_machine(self):
        next_machine = None
        min_queue_size = float('inf')
        for machine in self.machines:
            queue_size = len(machine.queue)
            if not machine.queue.full():
                if queue_size < min_queue_size:
                    min_queue_size = queue_size
                    next_machine = machine
        if next_machine is None:
            # all machine queues are full, raise an exception
            raise Exception('All machine queues are full')
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
