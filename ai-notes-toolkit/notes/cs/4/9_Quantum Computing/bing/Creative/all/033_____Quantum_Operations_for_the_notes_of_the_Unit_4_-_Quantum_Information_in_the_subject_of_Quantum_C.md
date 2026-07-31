# Quantum Operations

Quantum operations are transformations that a quantum mechanical system can undergo. They are used to manipulate quantum bits (qubits) in a quantum circuit. Quantum operations can be classified into two types: unitary and non-unitary.

## Unitary Operations

Unitary operations are reversible and preserve the total probability of the quantum state. They are represented by unitary matrices, which satisfy UU† = U†U = I, where U† is the conjugate transpose of U and I is the identity matrix. Unitary operations can be implemented by quantum gates, which are the building blocks of quantum circuits. Some examples of quantum gates are:

- Pauli-X gate: Flips the state of a qubit from |0> to |1> or vice versa. It is equivalent to a classical NOT gate. It is represented by the matrix:

|0 1|
|1 0|

- Pauli-Y gate: Flips the state of a qubit and adds a phase of i or -i. It is represented by the matrix:

|0 -i|
|i 0|

- Pauli-Z gate: Changes the phase of a qubit by π if it is in the state |1>. It is equivalent to a classical phase flip. It is represented by the matrix:

|1 0|
|0 -1|

- Hadamard gate: Creates a superposition of |0> and |1> with equal probabilities. It is represented by the matrix:

|1/√2 1/√2|
|1/√2 -1/√2|

- CNOT gate: Flips the state of a target qubit if the control qubit is in the state |1>. It is equivalent to a classical XOR gate. It is represented by the matrix:

|1 0 0 0|
|0 1 0 0|
|0 0 0 1|
|0 0 1 0|

## Non-Unitary Operations

Non-unitary operations are irreversible and do not preserve the total probability of the quantum state. They are represented by completely positive trace-preserving (CPTP) maps, which are linear maps from the set of density operators to itself. Non-unitary operations can be implemented by quantum measurements, which collapse the quantum state to a definite outcome with some probability. Some examples of quantum measurements are:

- Projective measurement: Projects the quantum state onto a basis of orthogonal vectors. The outcome is one of the basis vectors with a probability equal to the square of its amplitude. The quantum state after the measurement is the normalized outcome vector.

- POVM measurement: Performs a positive operator-valued measure (POVM) on the quantum state. The outcome is one of the POVM elements with a probability equal to the expectation value of the element. The quantum state after the measurement is the normalized POVM element applied to the state.

- QND measurement: Performs a quantum non-demolition (QND) measurement on the quantum state. The outcome is the eigenvalue of an observable that commutes with the Hamiltonian of the system. The quantum state after the measurement is the same as before, except for a phase factor.