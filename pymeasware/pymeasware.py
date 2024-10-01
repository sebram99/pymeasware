from abc import ABC, abstractmethod

class Generic(ABC):

    def __init__(self, instrument_type, resource_name):
        self.instrument_type = instrument_type
        self.resource_name = resource_name

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass

    @abstractmethod
    def clean(self):
        pass