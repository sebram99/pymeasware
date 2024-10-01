from pymeasware import Instrument

power_meter = Instrument.create_instrument("KeysightU2004B", "resource_name")
signal_generator = Instrument.create_instrument("HP8694B", "resource_name")

print(power_meter.get_info())
print(signal_generator.get_info())