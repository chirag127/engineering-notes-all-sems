### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or other sources of error.
- QEC codes encode a logical qubit (the unit of quantum information) into a larger number of physical qubits, such that errors can be detected and corrected without disturbing the logical qubit.
- The Shor code is one of the first and simplest QEC codes, discovered by Peter Shor in 1995  . It encodes one logical qubit into nine physical qubits, and can correct any single-qubit error (bit flip, phase flip, or both).
- The Shor code works as follows :
  - The logical qubit is initially stored in the first physical qubit.
  - Three CNOT gates are applied to copy the logical qubit to the third and sixth physical qubits. These qubits are used for correcting bit flip errors.
  - Three Hadamard gates are applied to the first, fourth, and seventh physical qubits. These qubits are used for correcting phase flip errors.
  - Three CNOT gates are applied to copy the first qubit to the fourth and seventh qubits, and the third qubit to the fifth and eighth qubits, and the sixth qubit to the ninth qubit. These qubits form three blocks of three qubits each, which are entangled in a superposition of states.
  - To detect and correct errors, syndrome measurements are performed on each block of three qubits, using ancillary qubits and controlled-NOT gates. The syndrome measurement does not disturb the logical qubit, but reveals information about the error.
  - Depending on the outcome of the syndrome measurement, appropriate correction operations are applied to the physical qubits, such as X gates for bit flip errors and Z gates for phase flip errors.
  - To recover the logical qubit, the encoding process is reversed, using CNOT and Hadamard gates.
- The Shor code can correct any single-qubit error, but it cannot correct errors that affect more than one qubit, such as collective dephasing or leakage. Therefore, more advanced QEC codes are needed for practical applications of quantum computing.
- The Shor code is an example of a stabilizer code, which is a class of QEC codes that use stabilizer operators to define and manipulate the logical qubits. Stabilizer codes are widely used in quantum computing and quantum information theory.