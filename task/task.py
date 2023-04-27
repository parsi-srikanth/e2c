"""

TODO: implement get_exec_time() method

"""

from task import TaskType, UrgencyLevel, TaskStatus
from machine import Machine


class Task:
    def __init__(self) -> None:
        self._id: int
        self._type: TaskType
        self._exp_exec_time: float
        self._sim_exec_time: float
        self._hard_deadline: float
        self._soft_deadline: float
        self._urgency: UrgencyLevel
        self._assigned_machine: Machine/None
        self._cunsumed_energy: float
        self._wasted_energy: float
        self._deferred: int
        self._preempted: int
        self._status: TaskStatus = TaskStatus.ARRIVING
        # not in class diagram, what is the default status?

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError('Task id must be an integer')
        self._id = id

    @property
    def type(self) -> TaskType:
        return self._type

    @type.setter
    def type(self, type: TaskType):
        if not isinstance(type, TaskType):
            raise TypeError('Task type must be a pre-defined type')
        self._type = type

    @property
    def exp_exec_time(self) -> float:
        return self._exp_exec_time

    @exp_exec_time.setter
    def exp_exec_time(self, exp_exec_time: float):
        if not isinstance(exp_exec_time, float):
            raise TypeError('Expected execution time must be a float')
        self._exp_exec_time = exp_exec_time

    @property
    def sim_exec_time(self) -> float:
        return self._sim_exec_time

    @sim_exec_time.setter
    def sim_exec_time(self, sim_exec_time: float):
        if not isinstance(sim_exec_time, float):
            raise TypeError('Simulated execution time must be a float')
        self._sim_exec_time = sim_exec_time

    @property
    def hard_deadline(self) -> float:
        return self._hard_deadline

    @hard_deadline.setter
    def hard_deadline(self, hard_deadline: float):
        if not isinstance(hard_deadline, float):
            raise TypeError('Hard deadline must be a float')
        self._hard_deadline = hard_deadline

    @property
    def soft_deadline(self) -> float:
        return self._soft_deadline

    @soft_deadline.setter
    def soft_deadline(self, soft_deadline: float):
        if not isinstance(soft_deadline, float):
            raise TypeError('Soft deadline must be a float')
        self._soft_deadline = soft_deadline

    @property
    def urgency(self) -> UrgencyLevel:
        return self._urgency

    @urgency.setter
    def urgency(self, urgency: UrgencyLevel):
        if not isinstance(urgency, UrgencyLevel):
            raise TypeError('Urgency level must be a pre-defined level')
        self._urgency = urgency

    @property
    def assigned_machine(self) -> Machine/None:
        return self._assigned_machine

    @assigned_machine.setter
    def assigned_machine(self, assigned_machine: Machine/None):
        if not isinstance(assigned_machine, Machine/None):
            raise TypeError('Assigned machine must be a machine or None')
        self._assigned_machine = assigned_machine

    @property
    def consumed_energy(self) -> float:
        return self._consumed_energy

    @consumed_energy.setter
    def consumed_energy(self, consumed_energy: float):
        if not isinstance(consumed_energy, float):
            raise TypeError('Consumed energy must be a float')
        self._consumed_energy = consumed_energy

    @property
    def wasted_energy(self) -> float:
        return self._wasted_energy

    @wasted_energy.setter
    def wasted_energy(self, wasted_energy: float):
        if not isinstance(wasted_energy, float):
            raise TypeError('Wasted energy must be a float')
        self._wasted_energy = wasted_energy

    @property
    def deferred(self) -> int:
        return self._deferred

    @deferred.setter
    def deferred(self, deferred: int):
        if not isinstance(deferred, int):
            raise TypeError('Deferred must be an integer')
        self._deferred = deferred

    @property
    def preempted(self) -> int:
        return self._preempted

    @preempted.setter
    def preempted(self, preempted: int):
        if not isinstance(preempted, int):
            raise TypeError('Preempted must be an integer')
        self._preempted = preempted

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, status: TaskStatus):
        if not isinstance(status, TaskStatus):
            raise TypeError('Task status must be a pre-defined status')
        self._status = status
