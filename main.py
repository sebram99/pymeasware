from pymeasware import Instrument

find_instrument = Instrument.find_instruments()
power_meter = Instrument.create_instrument("KeysightU2004A", find_instrument["U2004A"])

print(power_meter.get_info())