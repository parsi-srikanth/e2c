"""

TODO: add description

"""

from task_type import TaskType
from urgency_level import UrgencyLevel
from machine.machine import Machine
from typing import Dict                 #i think i need to import this for type annotating _ps_time
                                       
class Task:
    """
    
    TODO: add description

    """
        
    count = 0

    def __init__(self, task_type: TaskType, urgency: UrgencyLevel, assigned_machine: Machine):
        Task.count += 1
        self.id: int = Task.count
        # self._exp_exec_time: list[float] = 
        # self._sim_exec_time: list[float] =
        # self._hard_deadline: float = 
        # self._soft_deadline: float = 
        # self._urgency : UrgencyLevel = urgency
        # self._ps_time: Dict[str, float] = {   #init to 0.0 for now, unsure what to set to
        #                 "arrival": 0.0,
        #                 "start": 0.0,
        #                 "preemption": 0.0,
        #                 "completion": 0.0,
        #                 "cancel": 0.0,
        #                 "drop": 0.0
        #                 }
        # self._assigned_machine: Machine/None = assigned_machine
        # self._consumed_energy: float = 
        # self._wasted_energy: float = 
        # self._deferred: int = 
        # self._preempted: int = 
