# Alice and Bob Quantum Plugin Wrapper for PennyLane

## Overview
This repository serves as an unofficial PennyLane wrapper for the Alice and Bob Quantum Plugin, initially developed for Qiskit as detailed in the Alice&Bob Qiskit Provider. This wrapper extends the compatibility of the original Qiskit-based plugin to the PennyLane quantum computing framework, enabling users to leverage the unique features of the Alice and Bob Quantum Plugin within PennyLane's ecosystem. 

## Features
- Smooth integration with PennyLane, enhancing its quantum computing capabilities.
- Access to a variety of unique features offered by the Alice and Bob Quantum Plugin.
- Supports multiple backends, including:
  - EMU:6Q:PHYSICAL_CATS
  - EMU:40Q:PHYSICAL_CATS
  - EMU:40Q:LOGICAL_TARGET
  - EMU:15Q:LOGICAL_EARLY
  - EMU:1Q:LESCANNE_2020

## Example Use Cases
The following examples demonstrate how to configure the Alice and Bob Quantum Plugin within the PennyLane environment:


### Local Alice & Bob simulator (no API token required)

```python
dev = qml.device("alicebob.qubit", wires=1, shots=10, alice_backend="EMU:40Q:PHYSICAL_CATS", average_nb_photons=4, kappa_2=1e4)
```

** For detailed information on the specialized parameters, please consult the repository for the Qiskit Alice and Bob provider.

### Alice & Bob quantum hardware (API token required)

```python
dev = qml.device("alicebob.qubit", wires=1, shots=10, alice_backend="EMU:1Q:LESCANNE_2020", api_token="MY_API_TOKEN")
```

### Complete Example

You can find a complete example in the [examples folder](./examples/sample_circuit.ipynb). In this example we show how to use the Alice and Bob Quantum Plugin with PennyLane to run a simple quantum circuit on multiple backends and perform a simple Grover search.


## Installation
Install the wrapper with ease by executing the following command:

```bash
pip install git+https://github.com/QuantumETS/pennylane-alice-bob.git@main
```