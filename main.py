from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox
from PyQt6.QtCore import QTimer
from pymeasware import Instrument

class PowerMeterUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Power Meter Monitor")
        self.setGeometry(100, 100, 400, 300)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Instrument selection
        self.instrument_combo = QComboBox()
        self.refresh_button = QPushButton("Refresh Instruments")
        self.refresh_button.clicked.connect(self.refresh_instruments)

        # Readings display
        self.power_label = QLabel("Power: --")
        self.frequency_label = QLabel("Frequency: --")
        self.status_label = QLabel("Status: Not Connected")

        # Controls
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_instrument)
        
        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)
        self.start_button.setEnabled(False)

        # Add widgets to layout
        layout.addWidget(self.instrument_combo)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.start_button)
        layout.addWidget(self.power_label)
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.status_label)

        # Setup timer for continuous readings
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_readings)
        
        # Initialize instrument
        self.power_meter = None
        self.refresh_instruments()

    def refresh_instruments(self):
        """Find and populate available instruments"""
        self.instrument_combo.clear()
        available_instruments = Instrument.find_instruments()
        
        for manufacturer, resource in available_instruments.items():
            self.instrument_combo.addItem(f"{manufacturer} ({resource})", resource)
        
        self.status_label.setText("Status: Select an instrument")

    def connect_instrument(self):
        """Connect to the selected instrument"""
        try:
            resource_name = self.instrument_combo.currentData()
            if not resource_name:
                self.status_label.setText("Status: No instrument selected")
                return

            self.power_meter = Instrument.create_instrument(
                instrument_type="KeysightU2004A",
                resource_name=resource_name
            )

            info = self.power_meter.get_info()
            self.status_label.setText(f"Status: Connected to {info}")
            self.start_button.setEnabled(True)

        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")
            self.start_button.setEnabled(False)

    def start_monitoring(self):
        """Start/Stop continuous monitoring"""
        if self.update_timer.isActive():
            self.update_timer.stop()
            self.start_button.setText("Start Monitoring")
            self.status_label.setText("Status: Monitoring stopped")
        else:
            self.update_timer.start(1000)  # Update every 1 second
            self.start_button.setText("Stop Monitoring")
            self.status_label.setText("Status: Monitoring active")

    def update_readings(self):
        """Update power readings"""
        try:
            if self.power_meter:
                power = self.power_meter.get_power()
                self.power_label.setText(f"Power: {power}")
        except Exception as e:
            self.status_label.setText(f"Status: Error - {str(e)}")
            self.update_timer.stop()
            self.start_button.setText("Start Monitoring")

if __name__ == '__main__':
    app = QApplication([])
    window = PowerMeterUI()
    window.show()
    app.exec()
