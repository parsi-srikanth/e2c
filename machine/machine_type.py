"""

TODO: add description

"""


class MachineType:
    """
    TODO: add description
    """
    id: int = 0

    def __init__(self) -> None:
        MachineType.id += 1
        self.id = MachineType.id
        self._name: str = f'M-{self.id}'
        self._dyn_power: float = 0.0
        self._idle_power: float = 0.0
        self._replicas: int = 1
        self._price: float = 0.0

    @classmethod
    def get_id(cls) -> int:
        return cls.id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if name in ['', ' ']:
            raise ValueError('Machine type name cannot be either empty or'
                             'space  string ')
        self._name = name

    @property
    def dyn_power(self) -> float:
        return self._dyn_power

    @dyn_power.setter
    def dyn_power(self, dyn_power) -> None:
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
    def idle_power(self, idle_power) -> None:
        if not isinstance(idle_power, float):
            raise TypeError('Idle power of the machine type must be a'
                            'float value')
        elif idle_power < 0:
            raise ValueError('Idle power of the machine type cannot be'
                             'a negative value')
        self._idle_power = idle_power

    @property
    def replicas(self) -> int:
        return self._replicas

    @replicas.setter
    def replicas(self, replicas) -> None:
        if not isinstance(replicas, int):
            raise TypeError('Replicas of the machine type must be an'
                            'integer value')
        elif replicas < 0:
            raise ValueError('Replicas of the machine type cannot be'
                             'a negative value')
        self._replicas = replicas

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price) -> None:
        if not isinstance(price, float):
            raise TypeError('Price of the machine type must be a'
                            'float value')
        elif price < 0:
            raise ValueError('Price of the machine type cannot be'
                             'a negative value')
        self._price = price
