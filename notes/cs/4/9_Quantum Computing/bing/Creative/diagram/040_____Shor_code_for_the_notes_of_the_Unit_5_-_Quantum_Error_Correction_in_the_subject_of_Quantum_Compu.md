# Unit 5 - Quantum Error Correction

## Shor code

- A quantum error correcting code that protects one logical qubit against arbitrary errors on one physical qubit  .
- It encodes one logical qubit into a highly entangled state of nine physical qubits .
- It consists of three steps: encoding, error detection and correction.
- Encoding: The logical qubit is first copied to the third and sixth qubits using CNOT gates, and then each block of three qubits is put into a superposition using Hadamard gates.
- Error detection: Each block of three qubits is measured using a parity check, which reveals the syndrome of the error without collapsing the logical qubit.
- Correction: Depending on the syndrome, a suitable correction operation is applied to the affected qubit to restore the logical qubit.
- The Shor code can correct any single-qubit error, including bit-flip, phase-flip and general errors.
- The Shor code is an example of a stabilizer code, which is a class of quantum error correcting codes that use stabilizer operators to detect and correct errors .
- The Shor code is also an example of a fault-tolerant code, which means that the encoding, error detection and correction operations can be performed without introducing additional errors.