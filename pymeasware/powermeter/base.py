from abc import abstractmethod
from ..base import Generic

class PowerMeter(Generic):
    """Base class for power meter instruments."""
    
    def __init__(self, instrument_type: str, resource_name: str):
        """
        Initialize the power meter.
        
        Args:
            instrument_type (str): Type of the power meter
            resource_name (str): VISA resource name
        """
        super().__init__(instrument_type, resource_name)

    @abstractmethod
    def get_power(self) -> str:
        """
        Get the current power reading.
        
        Returns:
            str: Power reading with unit
        """
        pass

    @abstractmethod
    def set_frequency(self, frequency: float) -> str:
        """
        Set the measurement frequency.
        
        Args:
            frequency (float): Frequency in Hz
            
        Returns:
            str: Confirmation message
        """
        pass

    @abstractmethod
    def calibrate(self):
        pass

