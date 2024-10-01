from abc import abstractmethod
from ..pymeasware import Generic

class PowerMeter(Generic):
    def __init__(self, instrument_type, resource_name):
        super().__init__(instrument_type, resource_name)

    @abstractmethod
    def get_power(self):
        pass

    @abstractmethod
    def set_frequency(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass

