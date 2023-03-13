Shannon entropy is a measure of the uncertainty or information content of a random variable. In quantum information theory, Shannon entropy can be generalized to quantum systems, where the random variable is replaced by a quantum state, and the probability distribution is replaced by the density matrix. Quantum error correction is a technique to protect quantum information from noise and decoherence by encoding it into larger quantum systems that can detect and correct errors. Quantum error correction can be understood in terms of quantum conditional and mutual entropies, which quantify the amount of information that can be extracted from or shared between quantum systems.

The following diagram illustrates the basic architecture of a quantum error correction scheme, using the example of a three-qubit bit-flip code. The diagram is drawn in ASCII art, using the following symbols:

- | and - for horizontal and vertical wires
- + for wire crossings
- O for qubits
- H for Hadamard gates
- X for Pauli-X gates
- Z for Pauli-Z gates
- C for controlled-NOT gates
- M for measurements
- S for syndrome bits
- R for recovery operations

The diagram shows how a single logical qubit (O) is encoded into three physical qubits (O O O) using Hadamard and CNOT gates, and how the encoded state is subjected to a possible bit-flip error (X) on any of the physical qubits. The error is detected by measuring the parity of two pairs of physical qubits (M M), which produces two syndrome bits (S S) that indicate the location of the error. The error is corrected by applying a conditional Pauli-X gate (R) on the affected qubit, depending on the syndrome bits. The corrected state is then decoded back to the original logical qubit (O) using the inverse of the encoding circuit.

```
    O
    |
    H
    |
    C
    |
    C
    |
    X
    |
    C
    |
    C
    |
    H
    |
    O
    |
+---+---+
|   |   |
H   H   H
|   |   |
C   |   |
|   C   |
|   |   C
|   |   |
X   X   X
|   |   |
C   |   |
|   C   |
|   |   C
|   |   |
H   H   H
|   |   |
+---+---+
|   |   |
M   M   |
|   |   |
S   S   |
|   |   |
+---+---+
|   |   |
R   R   R
|   |   |
+---+---+
|   |   |
O   O   O
|   |   |
+---+---+
    |
    O
```