"""

TODO: add description

"""
from power import EnergyModel


class Machine:
    def __init__(self):
        super().__init__()
        self.energyModel: EnergyModel = None
        self.queueSize(5)  # how to read from config file?
