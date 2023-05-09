"""
TODO: Add description
"""
from power.base_abs_energy_model import baseAbsEnergyModel
from machine.machine import Machine
from machine.machine_status import MachineStatus
from machine.machine_type import MachineType


class PowerDurationModel(baseAbsEnergyModel):
    """
    TODO: Add description
    """

    def __init__(self, machine: Machine) -> None:
        super().__init__(machine)

    def dyn_energy_consump(self, duration: float) -> float:
        """
        TODO: add description
        """
        dyn_power = self.machine.type.dyn_power
        energy_consumption = dyn_power * duration
        return energy_consumption

    def idle_energy_consump(self, duration: float) -> float:
        """
        TODO: add description
        """
        idle_power = self.machine.type.idle_power
        energy_consumption = idle_power * duration
        return energy_consumption
