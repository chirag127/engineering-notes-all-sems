### Control Operations for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Control operations are quantum operations that depend on the state of one or more control qubits, and perform some action on the target qubits. They are essential for implementing conditional logic and entanglement in quantum computing.
- One of the most common and important control operations is the controlled-NOT (CNOT) gate, which flips the target qubit if and only if the control qubit is in the state |1>. The CNOT gate can be represented by the following matrix:

| | | | |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |

- The CNOT gate can also be depicted by the following circuit diagram, where the control qubit is denoted by a dot and the target qubit is denoted by a cross:

```
|0> ---o--- |0>
|0> ---x--- |0>
```

- The CNOT gate can create entanglement between two qubits, for example, if the control qubit is in a superposition state such as |+> = (|0> + |1>)/sqrt(2), then applying the CNOT gate will result in the following state:

```
|+> ---o--- 1/sqrt(2) (|00> + |11>)
|0> ---x--- 1/sqrt(2) (|00> + |11>)
```

- This state is entangled, meaning that the qubits cannot be described independently, and measuring one qubit will affect the outcome of the other qubit.
- Another common control operation is the controlled-Z (CZ) gate, which applies a phase shift of -1 to the target qubit if and only if the control qubit is in the state |1>. The CZ gate can be represented by the following matrix:

| | | | |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | -1 |

- The CZ gate can also be depicted by the following circuit diagram, where the control qubit is denoted by a dot and the target qubit is denoted by a Z:

```
|0> ---o--- |0>
|0> ---Z--- |0>
```

- The CZ gate can also create entanglement between two qubits, for example, if the control qubit is in a superposition state such as |+>, then applying the CZ gate will result in the following state:

```
|+> ---o--- 1/sqrt(2) (|00> - |11>)
|0> ---Z--- 1/sqrt(2) (|00> - |11>)
```

- This state is also entangled, and it is equivalent to the previous state up to a local rotation of the target qubit by the Hadamard gate.
- More generally, any single-qubit gate U can be controlled by another qubit, resulting in a controlled-U (CU) gate, which applies U to the target qubit if and only if the control qubit is in the state |1>. The CU gate can be represented by the following matrix:

| | | | |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | U_00 | U_01 |
| 0 | 0 | U_10 | U_11 |

- The CU gate can also be depicted by the following circuit diagram, where the control qubit is denoted by a dot and the target qubit is denoted by a box with U inside:

```
|0> ---o--- |0>
|0> ---U--- |0>
```

- The CU gate can also create entanglement between two qubits, for example, if the control qubit is in a superposition state such as |+>, then applying the CU gate will result in the following state:

```
|+> ---o--- 1/sqrt(2) (|0