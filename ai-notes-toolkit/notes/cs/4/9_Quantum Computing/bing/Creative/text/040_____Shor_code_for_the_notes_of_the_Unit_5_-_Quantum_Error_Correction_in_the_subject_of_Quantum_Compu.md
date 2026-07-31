### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or other sources of error.
- QEC codes are based on encoding a logical qubit (the unit of quantum information) into a larger number of physical qubits, such that errors can be detected and corrected without disturbing the logical qubit.
- Shor code is one of the first and simplest QEC codes, proposed by Peter Shor in 1995  . It encodes one logical qubit into nine physical qubits, and can correct any single-qubit error (bit-flip, phase-flip, or both).
- Shor code works by first transferring the state of the logical qubit to three physical qubits using CNOT gates, then applying Hadamard gates to each of the three qubits to create a superposition of states. This process is repeated three times to obtain nine physical qubits in a highly entangled state.
- To detect and correct errors, Shor code uses syndrome measurements, which are multi-qubit measurements that do not disturb the logical qubit but reveal information about the error. The syndrome measurements consist of four parity checks: two for bit-flip errors and two for phase-flip errors.
- The parity checks are performed by applying CNOT gates between pairs of physical qubits and measuring the ancillary qubits. Depending on the outcome of the measurements, the error can be located and corrected by applying appropriate gates to the affected qubit.
- Shor code can also be generalized to encode more than one logical qubit, or to correct more than one error, by using larger blocks of physical qubits and more complex syndrome measurements. These codes are known as Bacon-Shor codes.
- Shor code and its variants are examples of stabilizer codes, which are a class of QEC codes that are defined by a set of operators that commute with the logical qubits and have eigenvalues of +1 or -1. The syndrome measurements are equivalent to measuring the eigenvalues of the stabilizer operators.
- Shor code can be implemented on a quantum computer using quantum circuits, such as the ones shown in the following figure:

![Shor code circuit](https://quantumcomputinguk.org/wp-content/uploads/2021/05/shor-code-circuit.png)

- The left circuit shows the encoding of the logical qubit into nine physical qubits, the middle circuit shows the syndrome measurement for bit-flip errors, and the right circuit shows the syndrome measurement for phase-flip errors. The correction gates are not shown, but they can be inferred from the measurement outcomes.