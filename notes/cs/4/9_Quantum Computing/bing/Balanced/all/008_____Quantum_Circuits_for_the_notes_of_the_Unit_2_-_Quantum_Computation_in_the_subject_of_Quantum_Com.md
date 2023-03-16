# Quantum Circuits

- A quantum circuit is a model for quantum computation, similar to classical circuits, in which a computation is a sequence of quantum gates, measurements, initializations of qubits to known values, and possibly other actions.
- A quantum gate is a basic unitary operation that acts on one or more qubits, such as the Hadamard gate, the Pauli-X gate, the CNOT gate, etc.
- A quantum wire is a line that carries a qubit from one gate to another, or to a measurement device.
- A quantum circuit can be represented by a diagram, where the horizontal axis is the time and the vertical axis is the qubits. Each gate is shown by a symbol, and each wire is shown by a line. For example, the following diagram shows a quantum circuit that applies a Hadamard gate to the first qubit, a CNOT gate to the first and second qubits, and then measures both qubits.

![quantum circuit example](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Simple-quantum-circuit.svg/1200px-Simple-quantum-circuit.svg.png)

- A quantum circuit can also be described by a unitary matrix, U, that maps the input state of the qubits to the output state of the qubits, before any measurement. For example, the unitary matrix for the above circuit is

![quantum circuit matrix](https://wikimedia.org/api/rest_v1/media/math/render/svg/8a0f0f0f5c5f5b5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f