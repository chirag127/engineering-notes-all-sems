## Unit 2 - Quantum Computation

Quantum computation is a model of computation that uses quantum mechanical phenomena, such as superposition and entanglement, to perform operations on data. Quantum computers are devices that can implement quantum computation.

One way to represent quantum computation is by using quantum circuit diagrams. A quantum circuit diagram is a graphical representation of a sequence of quantum operations on a set of qubits. A qubit is the basic unit of quantum information, which can exist in a superposition of two classical states, usually denoted as |0> and |1>.

A quantum circuit diagram consists of horizontal lines that represent qubits, and vertical or diagonal lines that represent quantum gates. Quantum gates are unitary transformations that manipulate one or more qubits. Some common quantum gates are:

- The Hadamard gate (H), which creates a superposition of |0> and |1> by rotating the qubit state by 90 degrees on the Bloch sphere.
- The Pauli-X gate (X), which flips the qubit state from |0> to |1> and vice versa, by rotating the qubit state by 180 degrees around the x-axis on the Bloch sphere.
- The Pauli-Z gate (Z), which changes the phase of the qubit state by 180 degrees, by rotating the qubit state by 180 degrees around the z-axis on the Bloch sphere.
- The controlled-NOT gate (CNOT), which flips the target qubit state if the control qubit state is |1>, and does nothing otherwise. This gate creates entanglement between the two qubits, which means their states are correlated and cannot be described independently.

The following diagram illustrates the basic architecture of a quantum circuit:

```
       ┌───┐     ┌───┐
q_0: ──┤ H ├──■──┤ X ├
       └───┘┌─┴─┐└─┬─┘
q_1: ───────┤ X ├──■──
            └───┘
```

This circuit applies a Hadamard gate to the first qubit (q_0), then a CNOT gate with q_0 as the control and q_1 as the target, and finally a Pauli-X gate to q_0. The output state of this circuit is |01>, which can be verified by applying the inverse operations in reverse order.

Quantum circuit diagrams can be drawn using various tools, such as Qiskit, Cirq, or LaTeX. The diagram above was drawn using Qiskit, which is an open-source, python-based quantum SDK developed by IBM. Qiskit has modules dedicated to finance, chemistry, optimization, and machine learning. It also allows users to execute quantum circuits on real or simulated quantum devices.