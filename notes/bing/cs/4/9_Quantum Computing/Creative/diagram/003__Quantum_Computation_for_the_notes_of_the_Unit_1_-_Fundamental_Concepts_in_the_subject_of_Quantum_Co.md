### Quantum Computation

Quantum computation is the process of using quantum systems, such as qubits, to perform operations that can be represented by quantum circuits. Quantum circuits are diagrams that show how qubits are manipulated by quantum gates and measured by classical devices. Quantum gates are unitary transformations that can change the state of one or more qubits. Measurement is the process of extracting classical information from a qubit or a qubit register.

The following diagram illustrates the basic architecture of a quantum computer:

```
+-----------------+     +-----------------+     +-----------------+
| Classical       |     | Quantum         |     | Classical       |
| Controller      |     | Processor       |     | Output          |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Classical   | |     | | Quantum     | |     | | Classical   | |
| | Program     | |     | | Circuit     | |     | | Result      | |
| | (Qiskit,    | |     | | (Qubits,    | |     | | (Bits)      | |
| | Cirq, etc.) | |     | | Gates, etc.)| |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Classical   | |     | | Quantum     | |     | | Classical   | |
| | Interface   | |---->| | Interface   | |---->| | Interface   | |
| | (API, SDK,  | |     | | (Pulses,    | |     | | (Post-      | |
| | etc.)       | |     | | Signals,    | |     | | processing, | |
| |             | |     | | etc.)       | |     | | etc.)       | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```