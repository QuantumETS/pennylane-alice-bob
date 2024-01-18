# Alice and Bob Quantum Plugin Wrapper for PennyLane

## Overview
This repository contains a non-official wrapper for the "Alice and Bob" Quantum Plugin, originally developed for Qiskit, now adapted for use with PennyLane. This wrapper allows users to leverage the unique features of the Alice and Bob Quantum Plugin within the PennyLane ecosystem.

## Features
- Seamless integration with PennyLane.
- Access to the unique quantum computing capabilities of the Alice and Bob Quantum Plugin.
- Available backends : 

    EMU:6Q:PHYSICAL_CATS 

    EMU:40Q:PHYSICAL_CATS 

    EMU:40Q:LOGICAL_TARGET 

    EMU:15Q:LOGICAL_EARLY 

    EMU:1Q:LESCANNE_2020 

## Usecases examples

```py
dev = qml.device("alicebob.simulator", wires=1,shots=10,alice_backend="EMU:40Q:PHYSICAL_CATS") # example to use local alice & bob simulator (no api_token)

dev = qml.device("alicebob.simulator", wires=1,shots=10,alice_backend="EMU:1Q:LESCANNE_2020",api_token="MY_API_TOKEN") # example to use alice & bob quantum hardware (has api_token)
```

## Installation
To install the wrapper, simply run:
```bash
pip install git+https://github.com/QuantumETS/pennylane-alice-bob.git@master
```

