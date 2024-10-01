from .pymeasware import Generic
from .powermeter  import KeysightU2004B
from .signalgenerator import HP8694B
import pyvisa

class Instrument:

    @staticmethod
    def create_instrument(instrument_type, resource_name):
        if instrument_type == "KeysightU2004B":
            return KeysightU2004B(resource_name)
        elif instrument_type == "HP8694B":
            return HP8694B(resource_name)
        else:
            return None

    @staticmethod
    def find_instruments():
        rm = pyvisa.ResourceManager()
        resources = rm.list_resources()
        instruments = {}

        for resource in resources:
            try:
                instr = rm.open_resource(resource)
                idn = instr.query('*IDN?')
                instruments[resource] = idn
            except Exception as e:
                instruments[resource] = str(e)

        return instruments