# Unit 5 - Quantum Error Correction

- Quantum error correction (QEC) is a set of methods to protect quantum information—that is, quantum states—from unwanted environmental interactions (decoherence) and other forms of noise .
- Quantum information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space. The code is designed to detect and correct errors that affect a subset of qubits, while preserving the encoded quantum information .
- Quantum error correction is essential to achieve fault-tolerant quantum computing, which can reduce the effects of noise on stored quantum information, faulty quantum gates, and faulty quantum measurements .
- Quantum error correction protocols consist of three main steps: encoding, syndrome measurement, and correction .
  - Encoding: The quantum information is encoded into a larger number of physical qubits using a quantum error-correcting code. The code defines a set of logical qubits, which are the qubits that carry the quantum information, and a set of stabilizer operators, which are used to detect errors.
  - Syndrome measurement: The stabilizer operators are measured periodically to obtain the syndrome, which is a set of classical bits that indicate the type and location of errors that have occurred on the physical qubits. The syndrome measurement does not disturb the logical qubits, as it only involves commuting operators.
  - Correction: Based on the syndrome, a recovery operation is applied to the physical qubits to correct the errors and restore the encoded quantum information. The recovery operation is chosen to be the inverse of the error that has occurred, or a close approximation of it.
- Quantum error correction codes can be classified into different types based on their properties, such as the number of qubits, the distance (the minimum number of qubits that need to be corrupted to cause an undetectable error), the rate (the ratio of logical qubits to physical qubits), and the type of errors they can correct .
  - Some examples of quantum error correction codes are:
    - Shor code: A 9-qubit code that can correct any single-qubit error. It is based on the classical repetition code and the quantum phase-flip code.
    - Steane code: A 7-qubit code that can correct any single-qubit error. It is based on the classical Hamming code and the quantum phase-flip code.
    - Surface code: A 2D lattice of qubits that can correct any local error. It is based on the toric code and the quantum phase-flip code.
    - Bacon-Shor code: A 2D array of qubits that can correct any error on a row or a column. It is based on the classical repetition code and the quantum phase-flip code.
    - CSS code: A general class of codes that can correct both bit-flip and phase-flip errors. It is based on two classical linear codes that satisfy certain conditions.
    - Stabilizer code: A general class of codes that can be defined by a set of stabilizer operators that commute with each other and with the logical operators. It is based on the theory of stabilizer groups and quantum error correction conditions.