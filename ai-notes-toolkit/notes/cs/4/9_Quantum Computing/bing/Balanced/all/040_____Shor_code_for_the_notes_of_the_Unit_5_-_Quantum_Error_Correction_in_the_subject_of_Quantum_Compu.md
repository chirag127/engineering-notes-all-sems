# Unit 5 - Quantum Error Correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- Quantum information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space.
- A quantum error-correcting code can correct errors if they affect only a small number of qubits, and if different errors can be distinguished by measuring some observables, called syndrome measurements.
- The most common types of errors in quantum computing are bit-flip errors, which flip the state of a qubit from |0> to |1> or vice versa, and phase-flip errors, which flip the sign of the phase of a qubit from |+> to |-> or vice versa.
- A simple example of a quantum error-correcting code is the three-qubit bit-flip code, which encodes a single logical qubit into three physical qubits, such that a bit-flip error on any one of them can be detected and corrected.
- A more general example of a quantum error-correcting code is the Shor code, which encodes a single logical qubit into nine physical qubits, and can correct both bit-flip and phase-flip errors on any one of them.
- A quantum error correction protocol consists of three steps: encoding, syndrome measurement, and correction.
- Encoding is the process of preparing the initial state of the logical qubits in the quantum error-correcting code.
- Syndrome measurement is the process of measuring some observables on the physical qubits to determine the type and location of the errors.
- Correction is the process of applying some unitary operations or measurements on the physical qubits to restore the state of the logical qubits.
- A quantum error correction protocol is said to be fault-tolerant if it can correct errors even if they occur during the encoding, syndrome measurement, or correction steps.
- A fault-tolerant quantum error correction protocol requires some additional resources, such as ancillary qubits, error-free gates, and error-free measurements.
- A long quantum computation will require many cycles of quantum error correction, each consisting of gates acting on encoded qubits, followed by syndrome measurements and corrections.
- The choice of quantum error correction code and protocol will influence the full quantum computing stack, from the layout of qubits at the physical level to gate compilation strategies at the software level.