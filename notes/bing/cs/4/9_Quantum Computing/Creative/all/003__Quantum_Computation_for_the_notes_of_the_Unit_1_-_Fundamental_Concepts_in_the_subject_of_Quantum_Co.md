### Quantum Computation for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

Quantum computation is a branch of computing that uses the principles of quantum mechanics to perform data operations. Quantum computation relies on quantum phenomena, such as quantum bits, superposition, and entanglement, to manipulate information in ways that are not possible with classical computers.

Some of the fundamental concepts of quantum computation are:

- **Quantum bits (qubits)**: A qubit is the basic unit of quantum information. Unlike a classical bit, which can only store a 0 or a 1, a qubit can store a superposition of both 0 and 1, meaning it can be in both states at the same time. A qubit can be represented by a vector in a two-dimensional complex space, called the Bloch sphere. A qubit can be realized by various physical systems, such as photons, electrons, atoms, or superconducting circuits.

- **Superposition**: Superposition is the ability of a quantum system to be in multiple states simultaneously. For example, a qubit can be in a superposition of 0 and 1, written as |0> + |1>, where |0> and |1> are the basis states of the qubit. The coefficients of the superposition, called amplitudes, are complex numbers that determine the probability of measuring the qubit in each state. The sum of the squares of the amplitudes must be equal to 1, which is known as the normalization condition.

- **Entanglement**: Entanglement is a quantum phenomenon that occurs when two or more qubits are correlated in such a way that their states cannot be described independently, even when they are physically separated. For example, two qubits can be entangled in a state called a Bell state, written as (|00> + |11>)/sqrt(2), where sqrt(2) is the normalization factor. This means that if one qubit is measured and found to be 0, the other qubit will also be 0, and vice versa. Entanglement is a key resource for quantum computation, as it enables quantum parallelism, quantum cryptography, and quantum teleportation.

- **Interference**: Interference is the phenomenon that occurs when two or more quantum states are combined, resulting in a new state that can be either constructive or destructive. For example, if two qubits are in a superposition of 0 and 1, and they are combined by a quantum gate, such as a Hadamard gate, the resulting state can be either |0> or |1>, depending on the relative phases of the amplitudes. Interference is essential for quantum computation, as it allows quantum algorithms to amplify the probability of the desired outcome and reduce the probability of the undesired outcome.

- **Quantum gates**: Quantum gates are the basic operations that can be performed on qubits. Quantum gates are analogous to classical logic gates, but they are reversible and unitary, meaning they preserve the information and the normalization of the qubits. Quantum gates can be represented by matrices that act on the qubit vectors. Some of the common quantum gates are:

  - **Pauli gates**: These are the simplest quantum gates that flip or rotate the qubits by 180 degrees. They are represented by the Pauli matrices, which are:

    - X gate: [[0, 1], [1, 0]]
    - Y gate: [[0, -i], [i, 0]]
    - Z gate: [[1, 0], [0, -1]]

  - **Hadamard gate**: This is a quantum gate that creates a superposition of 0 and 1 from a single qubit. It is represented by the Hadamard matrix, which is:

    - H gate: [[1, 1], [1, -1]]/sqrt(2)

  - **CNOT gate**: This is a quantum gate that performs a conditional flip on a target qubit, depending on the state of a control qubit. It is represented by the CNOT matrix, which is:

    - CNOT gate: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

- **Quantum circuits**: Quantum circuits are the diagrams that show the sequence of quantum gates applied to a set of qubits. Quantum circuits are read from left to right, with the input q