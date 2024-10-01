from pymeasware import Instrument

power_meter = Instrument.create_instrument("Power Meter", "resource_name")

print(power_meter.get_info())