"""
This module contains the device class for constructing Alice & Bob's custom devices for PennyLane.
"""
import warnings
from pennylane import QubitDevice, DeviceError
import pennylane as qml
from qiskit_alice_bob_provider.local.provider import AliceBobLocalProvider
from qiskit_alice_bob_provider import AliceBobRemoteProvider

class AliceBobSimulatorDevice(qml.devices.Device):
    """Alice & Bob's custom device for PennyLane."""

    name = "Alice & Bob's custom PennyLane plugin"
    short_name = "alicebob.simulator"
    pennylane_requires = ">=0.28.0"
    version = "0.0.1"
    author = "QuantumETS"

    def configured_backend(backend, api_key=''):
        for element in AliceBobLocalProvider().backends():
            if backend.strip() == element.name.strip():
                print(f"Using alice & bob {backend} backend...")
                if len(api_key) > 1:
                    backend = AliceBobRemoteProvider(api_key).get_backend(backend)
                else:
                    backend = AliceBobLocalProvider().get_backend(backend)
                break
        return backend

    def __init__(self,         
        wires=None,
        shots=None,
        seed="global",
        max_workers=None,
        api_token=""):
        pass
    def __new__(cls,
        wires=1,
        shots=1,
        seed="global",
        max_workers=None,
        alice_backend="EMU:6Q:PHYSICAL_CATS",
        api_token=""):
        provider = cls.configured_backend(alice_backend, api_token)

        class stub:
            n_qubits = 3
        def conf():
            return stub()
        
        provider.configuration = conf
        if provider == None:
            backend_names = ""
            for element in AliceBobLocalProvider().backends():
                backend_names += element.name + " "
            print(f"backend error, please choose one of following : {backend_names}")
            return None
        
        return qml.device('qiskit.remote', wires=wires, backend=provider,shots=shots)
