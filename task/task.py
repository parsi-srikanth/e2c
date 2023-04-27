"""

TODO: implement get_exec_time() method

"""

from task_type import TaskType
from urgency_level import UrgencyLevel
from machine.machine import Machine
from typing import Dict #i think i need to import this for type annotating _ps_time, but remove if unneeded
                                       
class Task:
    """
    
    TODO: add description

    """
        
    count = 0

    # def __init__(self, type: TaskType, hard_deadline: TaskType.hard_deadline, urgency: UrgencyLevel, assigned_machine: Machine):
    def __init__(self, type: TaskType, urgency: UrgencyLevel):
        Task.count += 1
        self.id: int = Task.count
        self._type: TaskType = type
        self._exp_exec_time: list[float] 
        self._sim_exec_time: list[float]
        # self._hard_deadline: float = hard_deadline
        self._hard_deadline: float
        self._soft_deadline: float 
        self._urgency : UrgencyLevel = urgency
        self._ps_time: Dict[str, float] = {  
                        "arrival",
                        "start",
                        "preemption",
                        "completion",
                        "cancel",
                        "drop"
                        }
        # self._assigned_machine: Machine/None = assigned_machine
        self._assigned_machine: Machine/None
        self._consumed_energy: float 
        self._wasted_energy: float 
        self._deferred: int 
        self._preempted: int


    @property
    def type(self) -> TaskType:
        return self._type

    @type.setter
    def type(self, type):
        if not isinstance(type, TaskType):
            raise ValueError('Task type of the task must'
                             'be of type TaskType')
        self._type = type

    @property
    def exp_exec_time(self) -> float:
        return self._exp_exec_time

    @exp_exec_time.setter
    def exp_exec_time(self, exp_exec_time):
        if not isinstance(exp_exec_time, float):
            raise ValueError('Expected execution time of the task must'
                             'be a float')
        elif exp_exec_time < 0:
            raise ValueError('Expected execution time of the task cannot'
                             'be a negative value')
        self._exp_exec_time = exp_exec_time

    @property
    def sim_exec_time(self) -> float:
        return self._sim_exec_time

    @sim_exec_time.setter
    def sim_exec_time(self, sim_exec_time):
        if not isinstance(sim_exec_time, float):
            raise ValueError('Expected execution time of the task must'
                             'be a float')
        elif sim_exec_time < 0:
            raise ValueError('Expected execution time of the task cannot'
                             'be a negative value')
        self._sim_exec_time = sim_exec_time
    
    @property
    def hard_deadline(self) -> float:
        return self._hard_deadline

    @hard_deadline.setter
    def hard_deadline(self, hard_deadline):
        if not isinstance(hard_deadline, float):
            raise ValueError('Hard deadline of the task must'
                             'be a float')
        elif hard_deadline < 0:
            raise ValueError('Hard deadline of the task cannot'
                             'be a negative value')
        self._hard_deadline = hard_deadline

    @property
    def soft_deadline(self) -> float:
        return self._soft_deadline

    @soft_deadline.setter
    def soft_deadline(self, soft_deadline):
        if not isinstance(soft_deadline, float):
            raise ValueError('Soft deadline of the task must'
                             'be a float')
        elif soft_deadline < 0:
            raise ValueError('Soft deadline of the task cannot'
                             'be a negative value')
        self._soft_deadline = soft_deadline

    @property
    def urgency(self) -> UrgencyLevel:
        return self._urgency

    @urgency.setter
    def urgency(self, urgency):
        if not isinstance(urgency, UrgencyLevel):
            raise ValueError('Urgency level of the task must'
                             'be of type UrgencyLevel')
        self._urgency = urgency

    @property
    def ps_time(self) -> Dict[str, float]:
        return self._ps_time

    @ps_time.setter
    def ps_time(self, ps_time):
        if not isinstance(ps_time, Dict[str, float]):
            raise ValueError('PS time of the task must'      #what does "ps" stand for?
                             'be of type Dict[str, float]')
        elif any(value < 0 for value in ps_time.values()):
            raise ValueError('PS times of the task cannot'
                             'be negative values')
        self._ps_time = ps_time

    @property
    def assigned_machine(self) -> Machine/None:
        return self._assigned_machine

    @assigned_machine.setter
    def assigned_machine(self, assigned_machine):
        if not isinstance(assigned_machine, Machine/None):
            raise ValueError('Assigned machine of the task'
                             'must be of type Machine or None')
        self._assigned_machine = assigned_machine

    @property
    def consumed_energy(self) -> float:
        return self._consumed_energy

    @consumed_energy.setter
    def consumed_energy(self, consumed_energy):
        if not isinstance(consumed_energy, float):
            raise ValueError('Consumed energy of the task'
                             'must be of type float')
        elif consumed_energy < 0:
            raise ValueError('Consumed energy of the task'
                             'cannot be a negative value')
        self._consumed_energy = consumed_energy

    @property
    def wasted_energy(self) -> float:
        return self._wasted_energy

    @wasted_energy.setter
    def wasted_energy(self, wasted_energy):
        if not isinstance(wasted_energy, float):
            raise ValueError('Wasted energy of the task'
                             'must be of type float')
        elif wasted_energy < 0:
            raise ValueError('Wasted energy of the task'
                            'cannot be a negative value')
        self._wasted_energy = wasted_energy

    @property
    def deferred(self) -> int:
        return self._deferred

    @deferred.setter
    def deferred(self, deferred):
        if not isinstance(deferred, int):
            raise ValueError('Deferred value of task'
                             'must be of type int')
        self._deferred = deferred

    @property
    def preempted(self) -> int:
        return self._preempted

    @preempted.setter
    def preempted(self, preempted) -> int:
        if not isinstance(preempted, int):
            raise ValueError('Preempted value of task'
                             'must be of type int')
        self._preempted = preempted