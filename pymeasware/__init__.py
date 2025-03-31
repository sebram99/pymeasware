from .base import Generic
from .powermeter import KeysightU2004A
from .signalgenerator import HP8694B
from .instrument_factory import InstrumentFactory
import pyvisa

__version__ = "0.1.0"
__all__ = ['Generic', 'KeysightU2004A', 'HP8694B', 'InstrumentFactory', 'Instrument']

class Instrument:
    """Main interface for instrument control."""
    
    @staticmethod
    def create_instrument(instrument_type: str, resource_name: str) -> Generic:
        """
        Create an instrument instance using the factory.
        
        Args:
            instrument_type (str): Type of instrument to create
            resource_name (str): VISA resource name
            
        Returns:
            Generic: An instance of the specified instrument
        """
        return InstrumentFactory.create_instrument(instrument_type, resource_name)

    @staticmethod
    def find_instruments() -> dict:
        """
        Find all available instruments.
        
        Returns:
            dict: Dictionary mapping manufacturer names to resource names
        """
        rm = pyvisa.ResourceManager()
        all_resources = rm.list_resources()
        # Filter for USB and GPIB resources
        resources = [resource for resource in all_resources 
                    if resource.startswith(('USB', 'GPIB'))]
        instruments = {}

        for resource in resources:
            try:
                instr = rm.open_resource(resource)
                instr.timeout = 1000
                idn = instr.query('*IDN?')
                manufacturer = idn.split(',')[1].strip()
                instruments[manufacturer] = resource
            except Exception as e:
                pass

        return instruments