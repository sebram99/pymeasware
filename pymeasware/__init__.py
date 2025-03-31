from .pymeasware import Generic
from .instrument_factory import InstrumentFactory
import pyvisa

__all__ = ['Generic', 'KeysightU2004A', 'HP8694B', 'InstrumentFactory', 'Instrument']

class Instrument:
    @staticmethod
    def create_instrument(instrument_type: str, resource_name: str) -> Generic:
        """Create an instrument instance using the factory."""
        return InstrumentFactory.create_instrument(instrument_type, resource_name)

    @staticmethod
    def find_instruments():
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