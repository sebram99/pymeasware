from .powermeter import PowerMeter

class KeysightU2004B(PowerMeter):
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
        return "Keysight U2004B Power Meter"

    def reset(self):
        return "Reset successful"

    def clean(self):
        return "Clean successful"