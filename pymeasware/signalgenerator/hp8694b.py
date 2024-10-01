from .signal_generator import SignalGenerator

class HP8694B(SignalGenerator):
    def __init__(self, resource_name):
        super().__init__("Signal Generator", resource_name)
        self.resource_manager = resource_name

    def set_frequency(self, frequency):
        return f"Frequency set to {frequency} Hz"

    def set_power(self, power):
        return f"Power set to {power} dBm"

    def set_output(self, output):
        return f"Output set to {output}"