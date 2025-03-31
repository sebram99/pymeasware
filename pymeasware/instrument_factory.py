from typing import Dict, Type
from .base import Generic
from .powermeter import KeysightU2004A
from .signalgenerator import HP8694B

class InstrumentFactory:
    _instruments: Dict[str, Type[Generic]] = {
        "KeysightU2004A": KeysightU2004A,
        "HP8694B": HP8694B,
    }

    @classmethod
    def register_instrument(cls, name: str, instrument_class: Type[Generic]) -> None:
        """Register a new instrument type with the factory."""
        cls._instruments[name] = instrument_class

    @classmethod
    def create_instrument(cls, instrument_type: str, resource_name: str) -> Generic:
        """Create an instance of the specified instrument type."""
        if instrument_type not in cls._instruments:
            raise ValueError(f"Unknown instrument type: {instrument_type}")
        
        return cls._instruments[instrument_type](resource_name)

    @classmethod
    def get_available_instruments(cls) -> list[str]:
        """Get a list of all registered instrument types."""
        return list(cls._instruments.keys()) 