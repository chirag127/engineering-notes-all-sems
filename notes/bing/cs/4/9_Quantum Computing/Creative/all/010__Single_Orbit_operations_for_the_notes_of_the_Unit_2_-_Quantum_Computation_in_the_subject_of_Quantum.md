### Single Qubit Operations for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Single qubit operations are fundamental operations that act as building blocks for quantum algorithms. They can manipulate the state of a single qubit by applying a unitary transformation to it.
- A unitary transformation is a linear transformation that preserves the norm of a vector, which means that the probability of measuring a qubit in any basis remains the same after applying the transformation.
- A unitary transformation can be represented by a 2x2 complex matrix U that satisfies UU* = I, where U* is the adjoint operation or the complex conjugate transpose of U, and I is the identity matrix.
- The adjoint operation is of crucial importance to quantum computing because it is needed to invert quantum transformations. If U is a unitary transformation, then U* is its inverse, which means that U*U = I.
- Single qubit operations, or single qubit quantum gates, can be classified into two categories: Clifford gates and non-Clifford gates.
- Non-Clifford gates consist only of the T-gate (also known as the π/8 gate), which is defined as:

T = [1 0; 0 e^(iπ/4)]

- The T-gate rotates the qubit by π/8 radians around the z-axis of the Bloch sphere, which is a geometric representation of the qubit state.
- The T-gate is important for quantum computation because it can introduce a phase difference between the |0> and |1> states of the qubit, which can be used to create interference and entanglement.
- Clifford gates are a set of single qubit gates that include the following:

  - The X-gate (also known as the NOT gate or the bit-flip gate), which is defined as:

  X = [0 1; 1 0]

  - The X-gate flips the state of the qubit, which means that it exchanges the |0> and |1> states.
  - The X-gate rotates the qubit by π radians around the x-axis of the Bloch sphere.

  - The Y-gate (also known as the bit-and-phase-flip gate), which is defined as:

  Y = [0 -i; i 0]

  - The Y-gate flips both the state and the phase of the qubit, which means that it exchanges the |0> and |1> states and adds a factor of -i to them.
  - The Y-gate rotates the qubit by π radians around the y-axis of the Bloch sphere.

  - The Z-gate (also known as the phase-flip gate), which is defined as:

  Z = [1 0; 0 -1]

  - The Z-gate flips the phase of the qubit, which means that it adds a factor of -1 to the |1> state.
  - The Z-gate rotates the qubit by π radians around the z-axis of the Bloch sphere.

  - The H-gate (also known as the Hadamard gate), which is defined as:

  H = (1/√2) [1 1; 1 -1]

  - The H-gate creates a superposition of the |0> and |1> states, which means that it maps the |0> state to (|0> + |1>)/√2 and the |1> state to (|0> - |1>)/√2.
  - The H-gate rotates the qubit by π/2 radians around the x-axis and then by π radians around the y-axis of the Bloch sphere.
  - The H-gate is important for quantum computation because it can create a balanced superposition of the computational basis states, which can be used to implement quantum algorithms such as Grover's search and quantum Fourier transform.

  - The S-gate (also known as the π/4 gate), which is defined as:

  S = [1 0; 0 i]

  - The S-gate rotates the qubit by π/4 radians around the z-axis of the Bloch sphere.
  - The S-gate is the square root of the Z-gate