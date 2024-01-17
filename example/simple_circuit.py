import pennylane as qml
from qiskit_alice_bob_provider import AliceBobRemoteProvider
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
from qiskit_alice_bob_provider.local.provider import AliceBobLocalProvider
from qiskit import QuantumCircuit, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
shots = 10000
provider = AliceBobLocalProvider()

circ = QuantumCircuit(2,2)
circ.reset(0)
circ.h(0)
circ.cx(0,1)
circ.measure(0,0)
circ.measure(1,1)

circ.draw('mpl')
plt.show()
#[<ProcessorSimulator(name=EMU:6Q:PHYSICAL_CATS)>, <ProcessorSimulator(name=EMU:40Q:PHYSICAL_CATS)>, <ProcessorSimulator(name=EMU:40Q:LOGICAL_TARGET)>, <ProcessorSimulator(name=EMU:15Q:LOGICAL_EARLY)>, <ProcessorSimulator(name=EMU:1Q:LESCANNE_2020)>]
for proc_simulator in provider.backends():
    print(proc_simulator.name)
# print("remote possible backends")
# ab = AliceBobRemoteProvider('MY_API_KEY')
# for proc_simulator in ab.backends():
#     print(proc_simulator.name)

def configured_backend(back):
    backend = AliceBobLocalProvider().get_backend(back)
    return backend

myapi="supge"
alice_backend='EMU:15Q:LOGICAL_EARLY'
dev = qml.device('qiskit.remote', wires=2, backend=configured_backend(alice_backend))