### Universal Quantum Gates

- A quantum gate is a basic quantum circuit operating on a small number of qubits.
- A quantum gate can perform a unitary transformation on the quantum state of the qubits.
- A set of universal quantum gates is any set of gates that can generate any unitary transformation on any number of qubits, up to a global phase .
- A universal quantum gate set is not unique, and there are many possible choices of such a set.
- One simple set of two-qubit universal quantum gates is the Hadamard gate (H), a phase rotation gate R (cos<sup>-1</sup>(3/5)), and the controlled-NOT gate (CNOT), a special case of controlled-U such that U = X.
- Another set of two-qubit universal quantum gates is the CNOT gate and any single-qubit gate.
- A single-gate set of universal quantum gates can also be formulated using the three-qubit Deutsch gate, D(θ), which is a generalization of the Toffoli gate.
- The Toffoli gate, or the controlled-controlled-NOT (CCNOT) gate, is a key logical gate in classical computing because it is universal for classical reversible computation.
- The Toffoli gate can be implemented using six CNOT gates and nine single-qubit gates.
- The iToffoli gate is a variant of the Toffoli gate that applies the inverse of the X gate on the target qubit if both control qubits are in the |1> state.
- The iToffoli gate can be implemented using a single step in a superconducting quantum information processor, and has a high fidelity of 0.993.