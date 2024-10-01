from abc import abstractmethod
from ..pymeasware import Generic

class SignalGenerator(Generic):
    def __init__(self, instrument_type, resource_name):
        super().__init__(instrument_type, resource_name)

    @abstractmethod
    def set_frequency(self):
        pass

    @abstractmethod
    def set_power(self):
        pass

    @abstractmethod
    def set_waveform(self):
        pass