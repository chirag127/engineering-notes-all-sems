### Single Orbit Operations

- Single orbit operations are quantum gates that act on a single qubit, which is the basic unit of quantum information.
- A single qubit can be represented by a two-dimensional complex vector, or a linear combination of two basis states, usually denoted as |0> and |1>.
- A single orbit operation can be represented by a 2x2 unitary matrix, which preserves the norm and the orthogonality of the qubit vector.
- A unitary matrix U satisfies UU^† = U^†U = I, where U^† is the adjoint or the complex conjugate transpose of U, and I is the identity matrix.
- A unitary matrix can be decomposed into a product of simpler matrices, such as the Pauli matrices, the Hadamard matrix, and the phase shift matrix.
- The Pauli matrices are X, Y, and Z, which correspond to the rotations of the qubit vector around the x, y, and z axes of the Bloch sphere, respectively. They are defined as:

X = |0><1| + |1><0| = [[0, 1], [1, 0]]

Y = -i|0><1| + i|1><0| = [[0, -i], [i, 0]]

Z = |0><0| - |1><1| = [[1, 0], [0, -1]]

- The Hadamard matrix H is a special case of the rotation matrix R_x(θ) around the x axis, with θ = π/2. It creates a superposition of the basis states, such that H|0> = (|0> + |1>)/√2 and H|1> = (|0> - |1>)/√2. It is defined as:

H = 1/√2 (|0><0| + |0><1| + |1><0| - |1><1|) = 1/√2 [[1, 1], [1, -1]]

- The phase shift matrix R_z(φ) is a special case of the rotation matrix R_z(φ) around the z axis, with φ being the phase angle. It adds a relative phase to the qubit vector, such that R_z(φ)|0> = |0> and R_z(φ)|1> = e^iφ |1>. It is defined as:

R_z(φ) = |0><0| + e^iφ |1><1| = [[1, 0], [0, e^iφ]]

- Single orbit operations can be used to manipulate the state of a single qubit, and to prepare it for further operations, such as measurement or entanglement with other qubits.
- Single orbit operations are reversible, meaning that they can be undone by applying their inverse or adjoint operation. For example, X^† = X, H^† = H, and R_z(φ)^† = R_z(-φ).
- Single orbit operations are also universal, meaning that any unitary matrix can be approximated by a finite sequence of single orbit operations. For example, any rotation matrix R(θ, n) around an arbitrary axis n can be decomposed into a product of X, Y, Z, and H matrices.