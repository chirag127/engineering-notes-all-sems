### Quantum Circuits

- A quantum circuit is a model for quantum computation, similar to classical circuits, in which a computation is a sequence of quantum gates, measurements, initializations of qubits to known values, and possibly other actions.
- A quantum circuit consists of quantum wires and quantum gates. Quantum wires are used to carry qubits, the basic units of quantum information, from one gate to another. Quantum gates are operations that manipulate one or more qubits, such as rotations, entanglements, or controlled operations.
- A quantum circuit can be represented by a diagram, where the horizontal lines are quantum wires and the boxes or symbols are quantum gates. The input qubits are on the left and the output qubits are on the right. For example, the following diagram shows a quantum circuit that applies a Hadamard gate to the first qubit, a CNOT gate to the first and second qubits, and a measurement to the second qubit.

```
  ┌───┐     ┌─┐
q0 ┤ H ├──■──┤M├
  └───┘┌─┴─┐└╥┘
q1 ────┤ X ├──╫─
       └───┘ ║ 
 c0 ──────────╩─
```

- A quantum circuit can be described by a unitary matrix, U, that maps the input state vector, |ψ⟩, to the output state vector, U|ψ⟩. The unitary matrix can be decomposed into a product of elementary matrices, each corresponding to a quantum gate. For example, the quantum circuit above can be described by the matrix U = M2 CNOT H1, where M2 is the measurement matrix, CNOT is the controlled-NOT matrix, and H1 is the Hadamard matrix acting on the first qubit.
- Quantum circuits are imperfect, which prevents us from running well-known quantum algorithms using the gates-based quantum computing approach. To overcome this problem, a new breed of quantum algorithms has been introduced, employing the parametrized shallow quantum circuits, which can be called variational (quantum) circuits. These circuits are designed to optimize a cost function that depends on the output of the circuit, and can be used for tasks such as quantum machine learning, quantum simulation, or quantum error correction.