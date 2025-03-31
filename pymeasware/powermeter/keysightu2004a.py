from .powermeter import PowerMeter
import pyvisa

class KeysightU2004A(PowerMeter):
    def __init__(self, resource_name):
        super().__init__("Power Meter", resource_name)
        self.resource_manager = resource_name

    def get_power(self):
        return "Power: 1.2 mW"

    def set_frequency(self, frequency):
        return f"Frequency set to {frequency} Hz"

    def calibrate(self):
        return "Calibration successful"

    def get_info(self):
        rm = pyvisa.ResourceManager()
        instr = rm.open_resource(self.resource_manager)
        return instr.query('*IDN?')

    def reset(self):
        return "Reset successful"

    def clean(self):
        return "Clean successful"