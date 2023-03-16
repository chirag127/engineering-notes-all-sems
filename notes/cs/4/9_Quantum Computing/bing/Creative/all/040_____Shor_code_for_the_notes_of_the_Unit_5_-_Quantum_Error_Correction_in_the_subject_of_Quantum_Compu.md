# Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or faulty operations  .
- QEC codes encode a logical qubit into a larger number of physical qubits, such that errors can be detected and corrected by performing syndrome measurements and recovery operations .
- Shor code is a QEC code that can correct any single-qubit error, such as bit-flip, phase-flip, or a combination of both .
- Shor code encodes one logical qubit into nine physical qubits, arranged in three blocks of three qubits each .
- The first block is used to correct bit-flip errors, by applying a three-qubit repetition code.
- The second and third blocks are used to correct phase-flip errors, by applying a three-qubit phase code.
- The phase code is obtained by applying Hadamard gates to the repetition code, which transforms bit-flip errors into phase-flip errors and vice versa.
- The encoding circuit for the Shor code is shown below:

![Shor code encoding circuit](https://quantumcomputinguk.org/wp-content/uploads/2021/03/shor-code-encoding-circuit.png)

- The decoding circuit for the Shor code is the reverse of the encoding circuit, with additional syndrome measurements and recovery operations.
- The syndrome measurements are performed by applying controlled-NOT and controlled-Z gates to the qubits in each block, and measuring the ancillary qubits.
- The recovery operations are performed by applying X or Z gates to the qubits in each block, depending on the syndrome outcomes.
- The decoding circuit for the Shor code is shown below:

![Shor code decoding circuit](https://quantumcomputinguk.org/wp-content/uploads/2021/03/shor-code-decoding-circuit.png)

- The Shor code can correct any single-qubit error, but it is not efficient, as it requires nine physical qubits for one logical qubit .
- There are other QEC codes that can achieve better error correction with fewer physical qubits, such as the Steane code, the Bacon-Shor code, or the surface code .