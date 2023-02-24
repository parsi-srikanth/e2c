"""
TODO: Add description
"""
from abs import ABC, abstractmethod

from clock import Clock
from machine.machine_type import MachineType
from machine.machine_status import MachineStatus


class baseAbsMachine(ABC):
    """
    TODO: Class description
    """

    def __init__(self, machine_type: MachineType) -> None:
        super().__init__()
        self._machine_type: MachineType = machine_type
        self._status: MachineStatus = MachineStatus.OFF        
        
    @property
    def machine_type(self) -> MachineType:
        return self._machine_type
    
    @machine_type.setter
    def machine_type(self, machine_type: MachineType):
        if not isinstance(machine_type, MachineType):
            raise TypeError('Machine type must be a pre-defined type')
        self._machine_type = machine_type

    @property
    def status(self) -> MachineStatus:
        return self._status

    @status.setter
    def status(self, machine_status: MachineStatus):
        if not isinstance(machine_status, MachineStatus):
            raise TypeError('Machine status is unknown')
        self._status = machine_status
    
    def start(self):
        self.status = MachineStatus.WORKING
    
    def shutdown(self):
        self.status = MachineStatus.OFF
