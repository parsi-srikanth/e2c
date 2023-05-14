import unittest
from loadbalancer import MM
from task.task import Task, TaskType
from machine.machine import Machine, MachineType
from scheduler.FCFS import FCFS


class TestMM(unittest.TestCase):

    def setUp(self):
        machine_type1 = MachineType()
        machine_type1.replicas = 2
        machine_type2 = MachineType()
        machine_type3 = MachineType()
        machine1 = Machine(machine_type1)
        machine1_b = Machine(machine_type1)
        machine2 = Machine(machine_type2)
        machine3 = Machine(machine_type3)
        machine1.scheduler = FCFS(machine1, 4)
        machine1.scheduler = FCFS(machine1_b, 4)
        machine2.scheduler = FCFS(machine1, 4)
        machine3.scheduler = FCFS(machine1, 4)
        t1 = TaskType()
        t2 = TaskType()
        t3 = TaskType()
        self.task1 = Task(t1, 0)
        self.task2 = Task(t2, 0)
        self.task3 = Task(t3, 0)
        self.task1.expected_execution_times.__setitem__(machine_type1, 7)
        self.task2.expected_execution_times.__setitem__(machine_type1, 5)
        self.task3.expected_execution_times.__setitem__(machine_type1, 8)
        self.task1.expected_execution_times.__setitem__(machine_type2, 5)
        self.task2.expected_execution_times.__setitem__(machine_type2, 8)
        self.task3.expected_execution_times.__setitem__(machine_type2, 9)
        self.task1.expected_execution_times.__setitem__(machine_type3, 12)
        self.task2.expected_execution_times.__setitem__(machine_type3, 10)
        self.task3.expected_execution_times.__setitem__(machine_type3, 9)

        machine1.scheduler.queue.put(Task(t1, 0))
        machine1.scheduler.queue.put(Task(t3, 0))
        machine1.scheduler.queue.put(Task(t3, 0))
        machine1_b.scheduler.queue.put(Task(t2, 0))
        machine1_b.scheduler.queue.put(Task(t2, 0))
        machine1_b.scheduler.queue.put(Task(t2, 0))
        machine2.scheduler.queue.put(Task(t1, 0))
        machine2.scheduler.queue.put(Task(t3, 0))
        machine3.scheduler.queue.put(Task(t3, 0))
        machine3.scheduler.queue.put(Task(t1, 0))
        machine3.scheduler.queue.put(Task(t1, 0))
        machine3.scheduler.queue.put(Task(t3, 0))
        self.machines = [machine1, machine1_b, machine2, machine3]

    def test_decide_multiple_tasks(self):
        mm = MM(self.machines, 3)
        mm.queue.add(self.task1)
        mm.queue.add(self.task2)
        mm.queue.add(self.task3)

        self.machines[1].assign_task.assert_called_with(self.task2)
        self.machines[2].assign_task.assert_called_with(self.task1)
        self.machines[2].assign_task.assert_called_with(self.task3)
