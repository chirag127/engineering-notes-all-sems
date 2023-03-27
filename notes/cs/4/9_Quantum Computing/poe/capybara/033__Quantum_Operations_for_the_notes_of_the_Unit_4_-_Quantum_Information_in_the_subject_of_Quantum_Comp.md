### Quantum Operations

Quantum operations or quantum gates are the basic building blocks of quantum circuits. They are similar to classical logic gates but operate on quantum bits or qubits, which can exist in a superposition of states.

Here are some commonly used quantum operations:

- **Hadamard gate (H):** This gate is used to create a superposition of states by transforming a qubit from the |0⟩ state to the |+⟩ state and from the |1⟩ state to the |-⟩ state. The Hadamard gate is represented by the matrix:

$$
H = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix}
$$

- **Pauli-X gate (X):** This gate is equivalent to a classical NOT gate, which flips the state of a qubit from |0⟩ to |1⟩ and vice versa. The Pauli-X gate is represented by the matrix:

$$
X = \begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}
$$

- **Pauli-Y gate (Y):** This gate is similar to the Pauli-X gate, but also introduces a phase shift. The Pauli-Y gate flips the state of a qubit from |0⟩ to i|1⟩ and from |1⟩ to -i|0⟩. The Pauli-Y gate is represented by the matrix:

$$
Y = \begin{bmatrix}
0 & -i \\
i & 0 \\
\end{bmatrix}
$$

- **Pauli-Z gate (Z):** This gate introduces a phase shift of π radians to a qubit in the |1⟩ state. The Pauli-Z gate leaves the |0⟩ state unchanged. The Pauli-Z gate is represented by the matrix:

$$
Z = \begin{bmatrix}
1 & 0 \\
0 & -1 \\
\end{bmatrix}
$$

- **CNOT gate:** The Controlled-NOT gate is a two-qubit gate that flips the second qubit if the first qubit is in the |1⟩ state. The CNOT gate is represented by the matrix:

$$
CNOT = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}
$$

These are just a few of the many quantum operations that can be used to build quantum circuits. By combining these gates in various ways, we can perform complex computations on quantum computers.