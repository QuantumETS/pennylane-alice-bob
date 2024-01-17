import pennylane as qml
# from qiskit_alice_bob_provider import AliceBobRemoteProvider
# from qiskit import QuantumCircuit, execute, transpile

# provider = AliceBobLocalProvider()
# print(provider.backends())
dev = qml.device("alicebob.simulator")

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    return qml.state()

print(circuit())


import pennylane as qml
dev = qml.device('qiskit.aer', wires=2)

@qml.qnode(dev)
def circuit(x, y, z):
    qml.RZ(z, wires=[0])
    qml.RY(y, wires=[0])
    qml.RX(x, wires=[0])
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(wires=1))
print(circuit(0.2, 0.1, 0.3))

tape = qml.tape.QuantumScript([qml.Hadamard(0)], [qml.counts(wires=0)],shots=1)

print(dev.execute(tape))