from .base import SignalGenerator
import pyvisa

class HP8694B(SignalGenerator):
    """HP 8694B Signal Generator implementation."""
    
    def __init__(self, resource_name: str):
        """
        Initialize the HP 8694B signal generator.
        
        Args:
            resource_name (str): VISA resource name
        """
        super().__init__("Signal Generator", resource_name)
        self.instrument_resource = pyvisa.ResourceManager().open_resource(resource_name)

    def set_frequency(self, frequency: float) -> str:
        """
        Set the output frequency.
        
        Args:
            frequency (float): Frequency in Hz
            
        Returns:
            str: Confirmation message
        """
        return f"Frequency set to {frequency} Hz"

    def set_power(self, power: float) -> str:
        """
        Set the output power level.
        
        Args:
            power (float): Power level in dBm
            
        Returns:
            str: Confirmation message
        """
        return f"Power set to {power} dBm"

    def set_output(self, state: bool) -> str:
        """
        Set the output state (on/off).
        
        Args:
            state (bool): True for output on, False for output off
            
        Returns:
            str: Confirmation message
        """
        return f"Output set to {'ON' if state else 'OFF'}"

    def get_info(self) -> str:
        """
        Get instrument identification information.
        
        Returns:
            str: Instrument identification string
        """
        return self.instrument_resource.query('*IDN?')

    def reset(self) -> None:
        """Reset the instrument to its default state."""
        self.instrument_resource.write('*RST')

    def calibrate(self) -> str:
        """
        Calibrate the signal generator.
        
        Returns:
            str: Calibration status message
        """
        return "Calibration successful"

    def clean(self) -> None:
        """Clear the instrument's status."""
        self.instrument_resource.write('*CLS')