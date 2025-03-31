from abc import ABC, abstractmethod

class Generic(ABC):
    """Base class for all measurement instruments."""
    
    def __init__(self, instrument_type: str, resource_name: str):
        """
        Initialize the instrument.
        
        Args:
            instrument_type (str): Type of the instrument
            resource_name (str): VISA resource name
        """
        self.instrument_type = instrument_type
        self.resource_name = resource_name

    @abstractmethod
    def get_info(self) -> str:
        """Get instrument identification information."""
        pass

    @abstractmethod
    def reset(self) -> None:
        """Reset the instrument to its default state."""
        pass

    @abstractmethod
    def calibrate(self) -> str:
        """Calibrate the instrument."""
        pass

    @abstractmethod
    def clean(self) -> None:
        """Clear the instrument's status."""
        pass 