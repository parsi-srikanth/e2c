"""
TODO: Add description
"""
from power.base_abs_energy_model import baseAbsEnergyModel


class PowerDurationModel(baseAbsEnergyModel):
    """
    TODO: Add description
    """

    #  Modified by : Srikanth
    def __init__(self, machine) -> None:
        super().__init__(machine)

    def calc_dyn_energy_consump(self, duration: float) -> float:
        """
        TODO: add description
        """
        dyn_power = self.machine.type.dyn_power
        energy_consumption = dyn_power * duration
        return energy_consumption

    def calc_idle_energy_consump(self, duration: float) -> float:
        """
        TODO: add description
        """
        idle_power = self.machine.type.idle_power
        energy_consumption = idle_power * duration
        return energy_consumption
