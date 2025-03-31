# PyMeasWare

PyMeasWare is a Python library for interfacing with measurement instruments using VISA (Virtual Instrument Software Architecture). It provides a simple and consistent interface for controlling various test and measurement equipment.

## Features

- Support for multiple instrument types (Power Meters, Signal Generators)
- Automatic instrument discovery
- Factory pattern for instrument creation
- VISA-based communication
- Extensible architecture for adding new instrument types

## Installation

```bash
pip install pymeasware
```

## Dependencies

- pyvisa
- (Add other dependencies as needed)

## Usage

### Basic Usage

```python
from pymeasware import Instrument

# Create a specific instrument
power_meter = Instrument.create_instrument("KeysightU2004A", "USB0::0x0957::0x0D07::MY12345678::INSTR")

# Find available instruments
available_instruments = Instrument.find_instruments()
```

### Available Instruments

Currently supported instruments:

- Power Meters:
  - Keysight U2004A
- Signal Generators:
  - HP 8694B

### Adding New Instruments

You can register new instrument types using the InstrumentFactory:

```python
from pymeasware import InstrumentFactory
from your_custom_instrument import CustomInstrument

InstrumentFactory.register_instrument("CustomInstrument", CustomInstrument)
```

## API Reference

### Instrument Class

The main interface for instrument control.

#### Methods

- `create_instrument(instrument_type: str, resource_name: str) -> Generic`
  - Creates a new instrument instance
  - Parameters:
    - `instrument_type`: String identifier for the instrument type
    - `resource_name`: VISA resource name
  - Returns: An instance of the specified instrument

- `find_instruments() -> dict`
  - Discovers available instruments
  - Returns: Dictionary mapping manufacturer names to resource names

### InstrumentFactory Class

Factory class for creating instrument instances.

#### Methods

- `register_instrument(name: str, instrument_class: Type[Generic]) -> None`
  - Registers a new instrument type
  - Parameters:
    - `name`: String identifier for the instrument type
    - `instrument_class`: Class implementing the instrument interface

- `create_instrument(instrument_type: str, resource_name: str) -> Generic`
  - Creates an instance of the specified instrument type
  - Parameters:
    - `instrument_type`: String identifier for the instrument type
    - `resource_name`: VISA resource name
  - Returns: An instance of the specified instrument

- `get_available_instruments() -> list[str]`
  - Returns a list of all registered instrument types

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]
