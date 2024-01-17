"""
This module contains the device class for constructing Alice & Bob's custom devices for PennyLane.
"""
import warnings
from pennylane import QubitDevice, DeviceError

class SimulatorDevice(QubitDevice):
    """Alice & Bob's custom device for PennyLane."""

    name = "Alice & Bob's custom PennyLane plugin"
    short_name = "alicebob.simulator"
    pennylane_requires = ">=0.34.0"
    version = "0.0.1"
    author = "QuantumETS"

    operations = {"PauliX", "RX", "CNOT"}
    observables = {"PauliZ", "PauliX", "PauliY", "Hadamard", "Identity"}


    def __init__(self, shots=1024, hardware_options=None):
        super().__init__(wires=24, shots=shots)
        self.hardware_options = hardware_options

    def apply(self, operation, **kwargs):
        if operation == "PauliX":
            self._apply_x(kwargs["wires"])
        elif operation == "RX":
            self._apply_rx(kwargs["wires"], kwargs["par"][0])
        elif operation == "CNOT":
            self._apply_cnot(kwargs["wires"][0], kwargs["wires"][1])

    def execute(self, observables, **kwargs):
        results = {}
        for o in observables:
            results[o] = 1.0

        return results