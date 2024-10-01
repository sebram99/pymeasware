from .pymeasware import Generic
from .powermeter  import KeysightU2004B

class Instrument:

    @staticmethod
    def create_instrument(instrument_type, resource_name):
        if instrument_type == "KeysightU2004B":
            return KeysightU2004B(resource_name)
        else:
            return None

