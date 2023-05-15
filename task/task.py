"""

TODO: add description

"""
from task.task_status import TaskStatus
from task.task_type import TaskType
from utils.descriptors import FloatDict, FloatDictFloatList, FloatList
import itertools


class Task:
    """
    TODO: add description
    """
    newid = itertools.count()

    def __init__(self, task_type: TaskType, arrival_time: float) -> None:
        self._id = next(Task.newid)
        self._type: TaskType = task_type
        self._status: TaskStatus = TaskStatus.ARRIVING
        self._deferred_count: int = 0
        self._preempted_count: int = 0
        self._time_pinpoint: FloatDictFloatList = FloatDictFloatList({
                                    'arrival': FloatList([arrival_time]),
                                    'start': FloatList([float('inf')]),
                                    'preeemption': FloatList([float('inf')]),
                                    'completion': FloatList([float('inf')]),
                                    'cancelation': FloatList([float('inf')]),
                                    'dropping': FloatList([float('inf')]),
                                    })
        self._execution_times: FloatDict = FloatDict()
        self._expected_execution_times: FloatDict = FloatDict()
        self._remaining_exec: float = None
        #  Modified by : Srikanth
        self._assigned_machine_id: int = None
        self._energy_usuage: float = 0.0
        self._wastaed_energy: bool = False
        self.deadline: float = (arrival_time + self._type.deadline)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id) -> None:
        if not isinstance(id, int):
            raise TypeError('Task ID must be an integer')
        self._id = id

    @property
    def type(self) -> TaskType:
        return self._type

    @type.setter
    def type(self, task_type: TaskType) -> None:
        if not isinstance(task_type, TaskType):
            raise TypeError('Type of the task must be a'
                            'TaskType value')
        self._type = task_type

    @property
    def status(self) -> TaskStatus:
        return self._status

    @status.setter
    def status(self, status: TaskStatus) -> None:
        if not isinstance(status, TaskStatus):
            raise TypeError('Status of the task must be a'
                            'TaskStatus value')
        self._status = status

    @property
    def deferred_count(self) -> int:
        return self._deferred_count

    @deferred_count.setter
    def deferred_count(self, deferred_count) -> None:
        if not isinstance(deferred_count, int):
            raise TypeError('Deferred count of the task must be an'
                            'integer value')
        elif deferred_count < self._deferred_count:
            raise ValueError('Deferred count of the task cannot be'
                             'set to a value less than the current value')
        self._deferred_count = deferred_count

    @property
    def preempted_count(self) -> int:
        return self._preempted_count

    @preempted_count.setter
    def preempted_count(self, preempted_count) -> None:
        if not isinstance(preempted_count, int):
            raise TypeError('Preempted count of the task must be an'
                            'integer value')
        elif preempted_count < self._preempted_count:
            raise ValueError('Preempted count of the task cannot be'
                             'set to a value less than the current value')
        self._preempted_count = preempted_count

    @property
    def time_pinpoint(self) -> FloatDict:
        return self._time_pinpoint

    @time_pinpoint.setter
    def time_pinpoint(self, time_pinpoint: FloatDict) -> None:
        if not isinstance(time_pinpoint, dict):
            raise TypeError('Time pinpoint of the task must be a'
                            'FloatDict value')
        self._time_pinpoint = FloatDict(time_pinpoint)

    @property
    def execution_times(self) -> FloatDict:
        return self._execution_times

    @execution_times.setter
    def execution_times(self, execution_times: FloatDict) -> None:
        if not isinstance(execution_times, FloatDict):
            raise TypeError('Execution times of the task must be a'
                            'FloatDict value')
        self._execution_times = FloatDict(execution_times)

    @property
    def expected_execution_times(self) -> FloatDict:
        return self._expected_execution_times

    @expected_execution_times.setter
    def expected_execution_times(self,
                                 expected_execution_times: FloatDict) -> None:
        if not isinstance(expected_execution_times, FloatDict):
            raise TypeError('Expected execution times of the task must be a'
                            'FloatDict value')
        self._expected_execution_times = FloatDict(expected_execution_times)

    @property
    def remaining_exec(self) -> float:
        return self._remaining_exec

    @remaining_exec.setter
    def remaining_exec(self, remaining_exec: float) -> None:
        if not (isinstance(remaining_exec, float) or None):
            raise TypeError('Remaining execution time of the task must be a'
                            'float value')
        elif remaining_exec < 0:
            raise ValueError('Remaining execution time of the task cannot be'
                             'a negative value')
        self._remaining_exec = remaining_exec

    #  Modified by : Srikanth
    @property
    def assigned_machine_id(self) -> int:
        return self._assigned_machine_id

    #  Modified by : Srikanth
    @assigned_machine_id.setter
    def assigned_machine_id(self, assigned_machine_id: int) -> None:
        if not isinstance(assigned_machine_id, int):
            raise TypeError('Assigned machine of the task must be a'
                            'int value')
        # check if assigned_machine_id is less than max machine id from config
        self._assigned_machine_id = assigned_machine_id

    @property
    def energy_usuage(self) -> float:
        return self._energy_usuage

    @energy_usuage.setter
    def energy_usuage(self, energy_usuage: float) -> None:
        if not isinstance(energy_usuage, float):
            raise TypeError('Energy usuage of the task must be a'
                            'float value')
        elif energy_usuage < 0:
            raise ValueError('Energy usuage of the task cannot be'
                             'a negative value')
        self._energy_usuage = energy_usuage

    @property
    def wastaed_energy(self) -> bool:
        return self._wastaed_energy

    @wastaed_energy.setter
    def wastaed_energy(self, wastaed_energy: bool) -> None:
        if not isinstance(wastaed_energy, bool):
            raise TypeError('Wastaed energy of the task must be a'
                            'bool value')
        self._wastaed_energy = wastaed_energy

    def __str__(self) -> str:
        return f'{self._type.name}-{self.id}'
