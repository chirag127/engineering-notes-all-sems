### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or faulty operations.
- QEC codes are based on encoding a logical qubit (the unit of quantum information) into a larger number of physical qubits, such that errors can be detected and corrected without disturbing the logical qubit.
- Shor code is one of the first and simplest QEC codes, proposed by Peter Shor in 1995 . It encodes one logical qubit into nine physical qubits, and can correct any single-qubit error (bit-flip, phase-flip, or both).
- Shor code works by first transferring the computational state of the main qubit to the 3rd and 6th qubit using CNOT gates. These qubits are used for correcting bit-flip errors.
- Then, the qubits are put into superposition using Hadamard gates, and the computational state of the main qubit is transferred to the 2nd and 5th qubit using CNOT gates. These qubits are used for correcting phase-flip errors.
- The resulting state is a highly entangled state of nine qubits, where the logical qubit is stored in the parity of the three groups of three qubits each.
- To detect and correct errors, syndrome measurements are performed on the nine qubits, using ancillary qubits and controlled gates. Syndrome measurements are multi-qubit measurements that do not disturb the logical qubit but retrieve information about the error.
- Depending on the syndrome measurement outcomes, the appropriate correction operations are applied to the qubits, such as X, Z, or Y gates, to restore the logical qubit state.
- Shor code can be generalized to encode k logical qubits into 2k+1 physical qubits, and can correct any single-qubit error or any error affecting at most k qubits .
- Shor code is an example of a stabilizer code, a class of QEC codes that are defined by a set of operators that commute with each other and with the logical operators.
- Shor code is also an example of a fault-tolerant (FT) code, a class of QEC codes that allow for FT operations, such as state preparation, state measurement, gates, and stabilizer measurement, that do not propagate or amplify errors.