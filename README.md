# Alice and Bob Quantum Plugin Wrapper for PennyLane

## Overview
This repository hosts an unofficial wrapper for the Alice and Bob Quantum Plugin, originally crafted for Qiskit and now made compatible with PennyLane. This integration facilitates the utilization of the distinctive functionalities of the Alice and Bob Quantum Plugin within PennyLane's quantum computing framework.

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
dev = qml.device("alicebob.qubit", wires=1, shots=10, alice_backend="EMU:40Q:PHYSICAL_CATS")
```

### Alice & Bob quantum hardware (API token required)

```python
dev = qml.device("alicebob.qubit", wires=1, shots=10, alice_backend="EMU:1Q:LESCANNE_2020", api_token="MY_API_TOKEN")
```

### Complete Example

You can find a complete example in the [examples folder](./examples/sample_circuit.ipynb). In this example we show how to use the Alice and Bob Quantum Plugin with PennyLane to run a simple quantum circuit on multiple backends and perform a simple Grover search.


## Installation
Install the wrapper with ease by executing the following command:

```bash
pip install git+https://github.com/QuantumETS/pennylane-alice-bob.git@master
```