from pymeasware import Instrument

instrument = Instrument.create_instrument("Power Meter", "resource_name")

print(instrument.get_info())
print(instrument.get_power())
print(instrument.set_frequency(1000))
print(instrument.calibrate())
print(instrument.reset())
print(instrument.clean())
