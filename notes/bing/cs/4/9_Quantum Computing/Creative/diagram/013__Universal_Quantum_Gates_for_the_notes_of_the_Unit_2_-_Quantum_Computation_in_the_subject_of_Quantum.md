A quantum gate is a basic quantum circuit operating on a small number of qubits. They are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits. A set of universal quantum gates is any set of gates to which any operation possible on a quantum computer can be reduced. One simple set of two-qubit universal quantum gates is the Hadamard gate (H), a phase rotation gate R (cos − 1 3 5)), and the controlled-NOT gate, a special case of controlled-U such that.

The following diagram illustrates the basic architecture of a quantum circuit using universal quantum gates:

```
|0> ---H---R---*---|0>
|0> ---H---H---X---|0>
```

The diagram uses the following symbols:

- |0> represents a qubit in the initial state of 0
- H represents the Hadamard gate, which creates a superposition of 0 and 1 states
- R represents the phase rotation gate, which adds a relative phase to the qubit state
- * represents the control qubit of the controlled-NOT gate, which flips the target qubit if the control qubit is 1
- X represents the target qubit of the controlled-NOT gate, which is also known as the NOT gate or the Pauli-X gate
- The horizontal lines represent the quantum wires that carry the qubits
- The vertical lines represent the quantum gates that act on the qubits