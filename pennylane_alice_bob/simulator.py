# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This module contains the :class:`~.AerDevice` class, a PennyLane device that allows
evaluation and differentiation of Qiskit Aer's C++ simulator
using PennyLan
"""
import qiskit_aer
from qiskit_alice_bob_provider import AliceBobLocalProvider
import os
from .device import QiskitDevice


class AliceBobSimulatorDevice(QiskitDevice):

    short_name = "alicebob.simulator"

    def __init__(
        self,
        wires,
        provider=None,
        backend="EMU:6Q:PHYSICAL_CATS",
        shots=1024,
        timeout_secs=None,
        **kwargs,
    ):
        provider = AliceBobLocalProvider()
        super().__init__(wires, provider=provider, backend=backend, shots=shots, **kwargs)
        