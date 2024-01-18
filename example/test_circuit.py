import pennylane as qml
from pennylane import numpy as np

# Create a device to execute the circuit on
dev = qml.device("alicebob.simulator", wires=1)

# Create a quantum circuit and qnode
@qml.qnode(dev)
def circuit():
    qml.PauliX(wires=0)
    return qml.probs()

# Execute the circuit
print(circuit())