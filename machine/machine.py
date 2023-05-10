"""

TODO: add description

"""
from machine.base_abs_machine import baseAbsMachine
from machine.machine_status import MachineStatus
from machine.machine_type import MachineType
from power.power_duration_model import PowerDurationModel
from task.task import Task
from task.task_status import TaskStatus
from event.event import Event
from event.event_type import EventType
from event.event_queue import EventQueue
from scheduler.FCFS import FCFS


class Machine(baseAbsMachine):
    """
    TODO: Add description
    """

    def __init__(self, machine_type: MachineType) -> None:
        super().__init__(machine_type)
        self.energy_model = PowerDurationModel(self)
        self.scheduler = FCFS(self)
        self.nxt_available_time = self.clk.time

    def execute(self, task: Task, time_slice: float) -> None:
        """
        TODO: Add description
        """
        if self.status == MachineStatus.WORKING:
            raise RuntimeError('Machine is already working')
        elif self.status == MachineStatus.OFF:
            raise RuntimeError('Machine is off')
        self.running_task = task
        task.status = TaskStatus.RUNNING
        self._status = MachineStatus.WORKING
        self.processed_tasks['executed'].append(task.id)
        task.time_pinpoint['start'].append(self.clk.time)
        if task.preempted_count == 0:
            no_interupt_completion_time = (task.time_pinpoint['start'][-1] +
                                           task.execution_times[self.type.id])
        else:
            no_interupt_completion_time = (task.time_pinpoint['start'][-1] +
                                           task.remaining_exec)
        if task.deadline <= task.time_pinpoint['start'][-1]:
            event_type = EventType.DROPPING
            event_time = task.time_pinpoint['start'][-1]
        elif time_slice >= task.execution_times[self.type.id]:
            if task.deadline >= no_interupt_completion_time:
                event_type = EventType.COMPLETION
                event_time = no_interupt_completion_time
            else:
                event_type = EventType.DROPPING
                event_time = task.deadline
        elif time_slice < task.deadline - task.time_pinpoint['start'][-1]:
            event_type = EventType.PREEMPTION
            event_time = task.time_pinpoint['start'][-1] + time_slice
        else:
            event_type = EventType.DROPPING
            event_time = task.deadline

        event = Event(event_type, event_time, task)
        EventQueue.add_event(event)
        self.nxt_available_time = event_time

    def drop(self) -> float:
        """
        TODO: Add description
        """
        task = self.running_task
        self.running_task = None
        self.processed_tasks['dropped'].append(task.id)
        task.status = TaskStatus.DROPPED
        self.status = MachineStatus.IDLE
        task.time_pinpoint['dropping'].append(self.clk.time)
        duration = (task.time_pinpoint['dropping'][-1] -
                    task.time_pinpoint['start'][-1])
        energy_consumption = self.energy_model.dyn_energy_consump(duration)
        self.energy_usuage['wasted'] += energy_consumption

        self.scheduler.scheduler()

        return energy_consumption

    def terminate(self) -> float:
        """
        TODO: Add description
        """

        task = self.running_task
        self.running_task = None
        self.processed_tasks['completed'].append(task.id)
        task.status = TaskStatus.COMPLETED
        self.status = MachineStatus.IDLE
        task.time_pinpoint['completion'].append(self.clk.time)
        duration = (task.time_pinpoint['completion'][-1] -
                    task.time_pinpoint['start'][-1])
        energy_consumption = self.energy_model.dyn_energy_consump(duration)
        self.energy_usuage['dynamic'] += energy_consumption

        return energy_consumption

    def preempt(self) -> float:
        """
        TODO: Add description
        """

        task = self.running_task
        self.running_task = None
        task.status = TaskStatus.PREEMPTED
        self.status = MachineStatus.IDLE
        task.time_pinpoint['preemption'].append(self.clk.time)
        duration = (task.time_pinpoint['preemption'][-1] -
                    task.time_pinpoint['start'][-1])
        if task.preempted_count == 0:
            task.remaining_exec = (task.execution_times[self.type.id] -
                                   duration)
        else:
            task.remaining_exec = (task.remaining_exec -
                                   duration)
        energy_consumption = self.energy_model.dyn_energy_consump(duration)
        task.preempted_count += 1

        return energy_consumption
