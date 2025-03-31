from abc import abstractmethod
from ..base import Generic

class SignalGenerator(Generic):
    """Base class for signal generator instruments."""
    
    def __init__(self, instrument_type: str, resource_name: str):
        """
        Initialize the signal generator.
        
        Args:
            instrument_type (str): Type of the signal generator
            resource_name (str): VISA resource name
        """
        super().__init__(instrument_type, resource_name)

    @abstractmethod
    def set_frequency(self, frequency: float) -> str:
        """
        Set the output frequency.
        
        Args:
            frequency (float): Frequency in Hz
            
        Returns:
            str: Confirmation message
        """
        pass

    @abstractmethod
    def set_power(self, power: float) -> str:
        """
        Set the output power level.
        
        Args:
            power (float): Power level in dBm
            
        Returns:
            str: Confirmation message
        """
        pass

    @abstractmethod
    def set_output(self, state: bool) -> str:
        """
        Set the output state (on/off).
        
        Args:
            state (bool): True for output on, False for output off
            
        Returns:
            str: Confirmation message
        """
        pass 