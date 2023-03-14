### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- A quantum error-correcting code is a unitary mapping of k qubits into a subspace of the quantum state space of n qubits such that if any t of the qubits undergo arbitrary decoherence, the resulting n qubits can be used to faithfully reconstruct the original quantum state of the k encoded qubits .
- Peter Shor first discovered a quantum error-correcting code by storing the information of one qubit onto a highly entangled state of nine qubits. A quantum error correcting code protects quantum information against errors of a limited form.
- The Shor code can correct both bit flip errors and phase flip errors, which are the most common types of errors in quantum computation.
- The Shor code works as follows:
  - The main qubit that we want to protect is encoded into three logical qubits, each of which is a three-qubit bit flip code.
  - The three logical qubits are then put into a superposition state using Hadamard gates, forming a three-qubit phase flip code.
  - After the encoding, an error may occur on any of the nine physical qubits, which can be a bit flip, a phase flip, or both.
  - To correct the error, we first apply the inverse of the encoding circuit, which reverses the Hadamard gates and the CNOT gates.
  - Then we measure the ancillary qubits to detect and correct any bit flip errors using Toffoli gates.
  - Finally, we apply the encoding circuit again, which corrects any phase flip errors using CNOT gates and Hadamard gates.
  - The resulting state is the same as the original state of the main qubit, up to a global phase.