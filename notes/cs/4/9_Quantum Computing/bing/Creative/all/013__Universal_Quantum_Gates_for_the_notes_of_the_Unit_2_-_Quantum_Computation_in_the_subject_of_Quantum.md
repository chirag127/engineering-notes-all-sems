### Universal Quantum Gates for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- A quantum gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits. 
- Unlike many classical logic gates, quantum logic gates are reversible. They are represented by unitary matrices, which preserve the norm of quantum states. 
- A universal quantum gate set is any set of gates to which any operation possible on a quantum computer can be reduced.  This means that any quantum circuit can be approximated arbitrarily well by a sequence of gates from the universal set. 
- One simple set of two-qubit universal quantum gates is the Hadamard gate (H), a phase rotation gate R (cos − 1 3 5), and the controlled-NOT gate (CNOT), a special case of controlled-U such that U = X. 
- The Hadamard gate (H) acts on a single qubit and creates a superposition of the basis states. It can be represented by the matrix:

```
H = 1/sqrt(2) * | 1  1 |
                | 1 -1 |
```

- The phase rotation gate R (cos − 1 3 5) acts on a single qubit and adds a relative phase of cos − 1 3 5 to the |1> state. It can be represented by the matrix:

```
R = | 1  0 |
    | 0  e^(i * cos^-1(3/5)) |
```

- The controlled-NOT gate (CNOT) acts on two qubits and flips the target qubit if the control qubit is |1>. It can be represented by the matrix:

```
CNOT = | 1 0 0 0 |
       | 0 1 0 0 |
       | 0 0 0 1 |
       | 0 0 1 0 |
```

- A mnemonic to remember the CNOT matrix is to think of it as a diagonal matrix with the last two elements swapped. 
- Another set of two-qubit universal quantum gates is the Toffoli gate (CCNOT) and any single-qubit gate. 
- The Toffoli gate (CCNOT) acts on three qubits and flips the target qubit if both control qubits are |1>. It can be represented by the matrix:

```
CCNOT = | 1 0 0 0 0 0 0 0 |
        | 0 1 0 0 0 0 0 0 |
        | 0 0 1 0 0 0 0 0 |
        | 0 0 0 1 0 0 0 0 |
        | 0 0 0 0 1 0 0 0 |
        | 0 0 0 0 0 1 0 0 |
        | 0 0 0 0 0 0 0 1 |
        | 0 0 0 0 0 0 1 0 |
```

- A mnemonic to remember the CCNOT matrix is to think of it as an identity matrix with the last two elements swapped. 
- A single-qubit gate can be any unitary matrix of dimension 2, such as the Pauli gates (X, Y, Z), the phase gate (S), the pi/8 gate (T), or any rotation gate (Rx, Ry, Rz). 
- A single-gate set of universal quantum gates can also be formulated using the three-qubit Deutsch gate, D(θ), which can be decomposed into CNOT and single-qubit gates.  
- The Deutsch gate D(θ) acts on three qubits and performs a controlled-controlled-rotation on the target qubit by an angle θ. It can be represented by the matrix:

```
D(θ) = | 1 0 0 0 0 0 0 0 |
       | 0 1 0 0 0 0 0 0 |
       | 0 0 1 0 0 0 0