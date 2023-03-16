# Universal Quantum Gates

- A quantum gate is a basic quantum circuit operating on a small number of qubits.
- A quantum gate is represented by a unitary matrix that preserves the norm of the quantum state.
- A set of quantum gates is universal if any quantum operation can be approximated by a sequence of gates from the set.
- A universal set of quantum gates can be used to construct any quantum algorithm or circuit.
- There are different ways to construct universal sets of quantum gates, depending on the number and type of gates involved.
- Some examples of universal sets of quantum gates are:
  - A single-qubit Hadamard gate (H), a single-qubit phase rotation gate (R), and a two-qubit controlled-NOT gate (CNOT).
  - A single-qubit π/8 gate (T), a single-qubit Hadamard gate (H), and a two-qubit controlled-NOT gate (CNOT).
  - A three-qubit Deutsch gate (D), which can be decomposed into CNOT and T gates.
  - A three-qubit Toffoli gate (CCNOT), which can be decomposed into CNOT, H, and T gates.
  - A three-qubit iToffoli gate, which is a modified version of the Toffoli gate that has higher fidelity and can be implemented natively in a superconducting quantum processor .