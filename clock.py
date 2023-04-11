"""

TODO: Add description

"""


class Clock(object):
    """
    TODO: Add description
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Clock, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._time = 0.0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, t):
        if t < 0.0:
            raise ValueError('Time cannot be negative')
        self._time = t

    def reset(self):
        self._time = 0
