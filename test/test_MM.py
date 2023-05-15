import unittest
from task.task import Task
from task.task_type import TaskType
from machine.machine import Machine, MachineType
from scheduler.FCFS import FCFS
from loadbalancer.MM import MM
from utils.descriptors import MachineList


class TestMM(unittest.TestCase):

    def setUp(self):
        machine_type1 = MachineType()
        machine_type1.replicas = 2
        machine_type2 = MachineType()
        machine_type3 = MachineType()
        machine1 = Machine(machine_type1, scheduler=FCFS)
        machine1_b = Machine(machine_type1, scheduler=FCFS)
        machine2 = Machine(machine_type2, scheduler=FCFS)
        machine3 = Machine(machine_type3, scheduler=FCFS)
        machine1.scheduler = FCFS(machine1, 4)
        machine1_b.scheduler = FCFS(machine1_b, 4)
        machine2.scheduler = FCFS(machine1, 4)
        machine3.scheduler = FCFS(machine1, 4)
        t1 = TaskType()
        t2 = TaskType()
        t3 = TaskType()
        self.task1 = Task(t1, 0)
        self.task2 = Task(t2, 0)
        self.task3 = Task(t3, 0)
        self.task1.expected_execution_times.__setitem__(machine_type1.id, 7)
        self.task2.expected_execution_times.__setitem__(machine_type1.id, 5)
        self.task3.expected_execution_times.__setitem__(machine_type1.id, 8)
        self.task1.expected_execution_times.__setitem__(machine_type2.id, 5)
        self.task2.expected_execution_times.__setitem__(machine_type2.id, 8)
        self.task3.expected_execution_times.__setitem__(machine_type2.id, 9)
        self.task1.expected_execution_times.__setitem__(machine_type3.id, 12)
        self.task2.expected_execution_times.__setitem__(machine_type3.id, 10)
        self.task3.expected_execution_times.__setitem__(machine_type3.id, 9)

        machine1.scheduler.queue.put(self.task1)
        machine1.scheduler.queue.put(self.task3)
        machine1.scheduler.queue.put(self.task3)
        machine1_b.scheduler.queue.put(self.task2)
        machine1_b.scheduler.queue.put(self.task2)
        machine1_b.scheduler.queue.put(self.task2)
        machine2.scheduler.queue.put(self.task1)
        machine2.scheduler.queue.put(self.task3)
        machine3.scheduler.queue.put(self.task3)
        machine3.scheduler.queue.put(self.task1)
        machine3.scheduler.queue.put(self.task1)
        machine3.scheduler.queue.put(self.task3)
        machine1.start()
        machine1_b.start()
        machine2.start()
        machine3.start()
        self.machines = MachineList((machine1, machine1_b, machine2, machine3))

    def test_decide_multiple_tasks(self):
        mm = MM(self.machines, 4)
        mm.queue.put(self.task1)
        mm.queue.put(self.task3)
        mm.queue.put(self.task2)

        mm.decide()

        assert self.task1.assigned_machine_id == \
            self.machines[2].machine_type.id
        assert self.task2.assigned_machine_id == \
            self.machines[1].machine_type.id
        assert self.task3.assigned_machine_id == \
            self.machines[2].machine_type.id
