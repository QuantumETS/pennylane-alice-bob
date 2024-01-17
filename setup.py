
import sys
import os
from setuptools import setup

with open("pennylane_alice_bob/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

requirements = ["pennylane>=0.15", "numpy", "python-dateutil", "requests"]

info = {
    # 'name' is the name that will be used by pip for installation
    "name": "PennyLane-AliceBob",
    "version": version,
    "maintainer": "Xanadu Inc.",
    "maintainer_email": "software@xanadu.ai",
    "url": "http://xanadu.ai",
    "license": "Apache License 2.0",
    "packages": ["pennylane_alice_bob"],
    "entry_points": {
        "pennylane.plugins": [
            "alicebob.simulator = pennylane_alice_bob:AliceBobSimulatorDevice",
        ]
    },
    "description": "PennyLane plugin for Alice & Bob hardware",
    "long_description": open("README.md").read(),
    "provides": ["pennylane_alice_bob"],
    "install_requires": requirements,
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    # Make sure to specify here the versions of Python supported
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Physics",
]

setup(classifiers=classifiers, **(info))
