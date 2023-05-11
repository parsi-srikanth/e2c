"""

TODO: add description

"""
from event.event import Event
from queue import Queue
from task.task import Task
from machine.machine import Machine


class FloatList(list):
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not (isinstance(value, float) or isinstance(value, int)):
                raise TypeError("All values of FloatList must be float")
            elif value < 0:
                raise ValueError("All values of FloatList must be positive")
        super().__init__(values)

    def append(self, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("All values of FloatList must be of type float")
        elif value < 0:
            raise ValueError("All values of FloatList must be positive")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not (isinstance(value, float) or isinstance(value, int)):
                raise TypeError("All values of FloatList must be float")
            elif value < 0:
                raise ValueError("All values of FloatList must be positive")
        super().extend(values)

    def insert(self, index, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("All values of FloatList must be float")
        elif value < 0:
            raise ValueError("All values of FloatList must be positive")
        super().insert(index, value)

    def __getitem__(self, index):
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("All values of FloatList must be of type float.")
        elif value < 0:
            raise ValueError("All values of FloatList must be positive")
        super().__setitem__(index, value)

    def __repr__(self):
        return super().__repr__()


class IntList(list):
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not isinstance(value, int):
                raise TypeError("All values of IntList must be int")
            elif value < 0:
                raise ValueError("All values of IntList must be positive")
        super().__init__(values)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("All values of IntList must be of type int")
        elif value < 0:
            raise ValueError("All values of IntList must be positive")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError("All values of IntList must be int")
            elif value < 0:
                raise ValueError("All values of IntList must be positive")
        super().extend(values)

    def insert(self, index, value):
        if not isinstance(value, int):
            raise TypeError("All values of IntList must be int")
        elif value < 0:
            raise ValueError("All values of IntList must be positive")
        super().insert(index, value)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("All values of IntList must be of type int.")
        elif value < 0:
            raise ValueError("All values of IntList must be positive")
        super().__setitem__(index, value)

    def __repr__(self):
        return super().__repr__()


class EventList(list):
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not isinstance(value, Event):
                raise TypeError("All values of EventList must be event type")
        super().__init__(values)

    def append(self, value):
        if not isinstance(value, Event):
            raise TypeError("All values of EventList must be event type")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not isinstance(value, Event):
                raise TypeError("All values of EventList must be event type")
        super().extend(values)

    def insert(self, index, value):
        if not isinstance(value, Event):
            raise TypeError("All values of EventList must be event type")
        super().insert(index, value)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Event):
            raise TypeError("All values of EventList must be event type")
        super().__setitem__(index, value)

    def __repr__(self):
        return super().__repr__()


class TaskList(list):
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not isinstance(value, Task):
                raise TypeError("All values of TaskList must be task type")
        super().__init__(values)

    def append(self, value):
        if not isinstance(value, Task):
            raise TypeError("All values of TaskList must be task type")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not isinstance(value, Task):
                raise TypeError("All values of TaskList must be task type")
        super().extend(values)

    def insert(self, index, value):
        if not isinstance(value, Task):
            raise TypeError("All values of TaskList must be task type")
        super().insert(index, value)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Task):
            raise TypeError("All values of TaskList must be task type")
        super().__setitem__(index, value)

    def __repr__(self):
        return super().__repr__()


class FloatDict(dict):
    def __setitem__(self, key, value):
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError('All elements in the list must be float type'
                            'float')
        elif value < 0:
            raise ValueError('All elements in the list must be positive')
        super().__setitem__(key, value)


class IntDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('All elements in the list must be integer')
        elif value < 0:
            raise ValueError('All elements in the list must be positive')
        super().__setitem__(key, value)


class IntDictIntList(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, IntList):
            raise TypeError('All elements in IntDictIntList must be IntList')
        super().__setitem__(key, value)


class FloatDictFloatList(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, FloatDict):
            raise TypeError('All elements in FloatDictFloatList must be'
                            'FloatDict')
        super().__setitem__(key, value)


class MachineList(list):
    def __init__(self, values=None):
        if values is None:
            values = []
        for value in values:
            if not isinstance(value, Machine):
                raise TypeError("Values of MachineList must be machine type")
        super().__init__(values)

    def append(self, value):
        if not isinstance(value, Machine):
            raise TypeError("Values of MachineList must be machine type")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not isinstance(value, Machine):
                raise TypeError("Values of MachineList must be machine type")
        super().extend(values)

    def insert(self, index, value):
        if not isinstance(value, Machine):
            raise TypeError("Values of MachineList must be machine type")
        super().insert(index, value)

    def __getitem__(self, index):
        return self._values[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Machine):
            raise TypeError("Values of MachineList must be machine type")
        super().__setitem__(index, value)

    def __repr__(self):
        return super().__repr__()


class QTask(Queue):

    def __init__(self, maxsize=0):
        super().__init__(maxsize=0)
        self.maxsize = maxsize
        self.list = []

    def put(self, item):
        if not isinstance(item, Task):
            raise TypeError("All values of QTask must be Task type")
        self.list.append(item)

    def get(self, index=0):
        try:
            self.list[index]
        except ValueError as val_err:
            raise ValueError(f'index {index} is out of range \
                of list {self.list} with error {val_err}')
        return self.list.pop(index)

    def remove(self, item):
        try:
            index = self.list.index(item)
        except ValueError as val_err:
            raise ValueError(f'index {index} is out of range \
                of list {self.list} with error {val_err}')
        self.list.pop(index)
