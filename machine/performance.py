"""
TODO: Add description

"""


class Performance:
    """
    TODO: add description
    """

    def __init__(self, machine_id: int) -> None:
        self._machine_id: int = machine_id
        # TODO : Add more machine info to this class

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
