"""
TODO: Add description

"""


class Performance:
    """
    TODO: add description
    """

    def __init__(self, machine_id: int) -> None:
        self._machine_id: int = machine_id
        self._completion_time: float = 0.0
        self._cpu_usage: float = 0.0
        self._energy_usage: float = 0.0
        self._throughput: float = 0.0
        self._latency: float = 0.0

    @property
    def machine_id(self) -> int:
        """
        TODO: Add description
        """
        return self._machine_id

    @id.setter
    def machine_id(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Machine id must be an integer value")
        self._machine_id = value

    def update(self) -> None:
        """
        TODO: Add description
        """
        pass

    def get_utilization(self) -> float:
        """
        TODO: Add description
        """
        pass

    def get_energy_usage(self) -> float:
        """
        TODO: Add description
        """
        pass

    def get_throughput(self) -> float:
        """
        TODO: Add description
        """
        pass

    def get_latency(self) -> float:
        """
        TODO: Add description
        """
        pass

    def get_cost(self) -> float:
        """
        TODO: Add description
        """
        pass
