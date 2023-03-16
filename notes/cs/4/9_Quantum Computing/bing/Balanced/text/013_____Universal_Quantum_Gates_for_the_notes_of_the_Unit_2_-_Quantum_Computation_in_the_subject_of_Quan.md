### Universal Quantum Gates

- A quantum gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits.
- A set of universal quantum gates is any set of gates to which any operation possible on a quantum computer can be reduced. In other words, any quantum circuit can be approximated arbitrarily well using only the gates from the universal set.
- One simple set of two-qubit universal quantum gates is the Hadamard gate (H), a phase rotation gate R (cos − 1 3 5)), and the controlled-NOT gate, a special case of controlled-U such that:

|H| = 1 √ 2 ( 1 1 1 − 1 ) , |R| = ( 1 0 0 e i cos − 1 3 5 ) , |CNOT| = ( 1 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 )

- A single-gate set of universal quantum gates can also be formulated using the three-qubit Deutsch gate, D(θ), which is defined as:

|D(θ)| = e i θ 8 ( 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 − 1 ) ( 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 ) ( 1 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 )

- Another important universal quantum gate is the Toffoli or the controlled-controlled-NOT (CCNOT) gate, which is a key logical gate in classical computing because it is universal, so it can build all logic circuits to compute any desired binary operation. The Toffoli gate can be implemented using six CNOT gates and nine single-qubit gates. The matrix representation of the Toffoli gate is:

|Toffoli| = ( 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0