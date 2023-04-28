"""

TODO: add description

"""
from abc import ABC


class MachineType(ABC):
    """
    TODO: add description
    """
    count = 0

    def __init__(self) -> None:
        MachineType.count += 1
        self.id: int = MachineType.count
        self._name: str = f'M-{self.id}'
        self._dyn_power: float = 0.0
        self._idle_power: float = 0.0
        self._replicas: int = 1

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        if name in ['', ' ']:
            raise ValueError('Machine type name cannot be either empty or'
                             'space  string ')
        self._name = name

    @property
    def dyn_power(self) -> float:
        return self._dyn_power

    @dyn_power.setter
    def dyn_power(self, dyn_power):
        if not isinstance(dyn_power, float):
            raise TypeError('Dynamic power of the machine type must be a'
                            'float value')
        elif dyn_power < 0:
            raise ValueError('Dynamic power of the machine type cannot be'
                             'a negative value')
        self._dyn_power = dyn_power

    @property
    def idle_power(self) -> float:
        return self._idle_power

    @idle_power.setter
    def idle_power(self, idle_power):
        if not isinstance(idle_power, float):
            raise TypeError('Idle power of the machine type must be a'
                            'float value')
        elif idle_power < 0:
            raise ValueError('Idle power of the machine type cannot be'
                             'a negative value')
        self._idle_power = idle_power
