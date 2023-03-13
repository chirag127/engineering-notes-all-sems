### Single Qubit Operations

- A single qubit operation is a transformation that acts on a single qubit, changing its state.
- A single qubit operation can be represented by a 2x2 unitary matrix, which preserves the norm and the orthogonality of the qubit state vector.
- A single qubit operation can also be represented by a rotation on the Bloch sphere, which is a geometric representation of the qubit state space.
- Some examples of single qubit operations are:

  - The identity operation, which does nothing to the qubit state. It is represented by the matrix I = [[1, 0], [0, 1]] or the identity rotation on the Bloch sphere.
  - The bit-flip operation, which flips the qubit state from |0> to |1> and vice versa. It is represented by the matrix X = [[0, 1], [1, 0]] or a rotation of pi radians around the x-axis on the Bloch sphere.
  - The phase-flip operation, which changes the sign of the qubit state from |0> to -|0> and from |1> to -|1>. It is represented by the matrix Z = [[1, 0], [0, -1]] or a rotation of pi radians around the z-axis on the Bloch sphere.
  - The Hadamard operation, which creates a superposition of |0> and |1> with equal amplitudes. It is represented by the matrix H = 1/sqrt(2) * [[1, 1], [1, -1]] or a rotation of pi/2 radians around the y-axis followed by a rotation of pi radians around the x-axis on the Bloch sphere.
  - The phase-shift operation, which adds a relative phase between |0> and |1>. It is represented by the matrix R = [[1, 0], [0, exp(i*theta)]] or a rotation of theta radians around the z-axis on the Bloch sphere.