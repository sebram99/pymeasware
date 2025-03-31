from .base import PowerMeter
import pyvisa

class KeysightU2004A(PowerMeter):
    def __init__(self, resource_name):
        super().__init__("Power Meter", resource_name)
        self.inst_resource = pyvisa.ResourceManager().open_resource(resource_name)
        self.inst_resource.timeout = 1000
        self.inst_resource.write('*RST')
        self.inst_resource.write('*CLS')

    def _check_error(self):
        error = self.inst_resource.query('SYST:ERR?;')
        error = error.split(',')
        error = [item.strip() for item in error]
        if error[0] != '+0':
            raise Exception(error[1])

    def get_power(self):
        power = self.inst_resource.query('FETC?;')
        power = power.strip()
        power = float(power)
        return power

    def set_frequency(self, frequency: float):
        self.inst_resource.write(f'FREQ {frequency}Hz')

    def calibrate(self, cal_type: str) -> bool:
        self.inst_resource.timeout = 40000

        if cal_type == "internal":
            self.inst_resource.write('CAL:ZERO:TYPE INT;:CAL;')
        elif cal_type == "external":
            self.inst_resource.write('CAL:ZERO:TYPE EXT;:CAL;')
        else:
            raise ValueError("Invalid calibration type")

        done = self.inst_resource.query('*OPC?;')
        done = done.strip()
        self.inst_resource.timeout = 5000
        return True if done == '1' else False

    def get_info(self) -> dict:
        info = self.inst_resource.query('*IDN?')
        info = info.split(',')
        info = [item.strip() for item in info]
        return {
            "Manufacturer": info[0],
            "Model": info[1],
            "Serial": info[2],
            "Firmware": info[3]
        }

    def reset(self):
        self.inst_resource.write('*RST')

    def clean(self):
        self.inst_resource.write('*CLS')