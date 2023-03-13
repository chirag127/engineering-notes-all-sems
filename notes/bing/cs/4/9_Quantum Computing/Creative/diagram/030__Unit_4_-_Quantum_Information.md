## Unit 4 - Quantum Information

Quantum information is the data that can be stored, measured, and manipulated in a quantum system, such as a qubit. A qubit is the basic unit of quantum information, analogous to a bit in classical computing. A qubit can exist in a superposition of two states, usually denoted as |0> and |1>, and can be manipulated by quantum gates, which are operations that change the state of the qubit. A quantum circuit is a diagram that shows how a sequence of quantum gates are applied to a set of qubits, and how the final state of the qubits can be measured.

The following diagram illustrates the basic architecture of a quantum circuit:

```
    |0>     |0>     |0>
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
    H       X       Z
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
    M       M       M
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     |       |       |
     v       v       v
    b0      b1      b2
```

In this diagram, each vertical line represents a qubit, and each horizontal line represents a quantum gate. The initial state of each qubit is |0>, and the final state is measured and stored in a classical bit, denoted as b0, b1, and b2. The quantum gates are labeled as H, X, and Z, which are the Hadamard, Pauli-X, and Pauli-Z gates, respectively. These gates perform the following transformations on the qubit state:

- H: |0> -> (|0> + |1>)/sqrt(2), |1> -> (|0> - |1>)/sqrt(2)
- X: |0> -> |1>, |1> -> |0>
- Z: |0> -> |0>, |1> -> -|1>

The measurement operation, denoted as M, collapses the qubit state to either |0> or |1>, with a probability determined by the amplitude of each state. The measurement result is then stored in a classical bit, which can be either 0 or 1.

The quantum circuit diagram can be used to visualize and analyze the quantum information processing that occurs in a quantum system, and to design and implement quantum algorithms and protocols. Quantum circuit diagrams are one of the main tools for quantum computing and quantum information theory.